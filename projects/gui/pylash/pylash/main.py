import dataclasses
import logging
import pathlib
import shutil
import sys
import textwrap
from pprint import pformat
from typing import Optional

from PySide6.QtCore import Slot
from PySide6.QtGui import QAction, QCloseEvent, QKeySequence, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QGraphicsScene,
    QGraphicsView,
    QHBoxLayout,
    QMessageBox,
    QPushButton,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)

from pylash import settings, unsplash  # isort: skip

# -------------
# Prerequisites
# -------------

logging.basicConfig(
    level=settings.DEBUG or logging.INFO,
    format=settings.LOG_FORMAT,
    style="{",
)
LOG = logging.getLogger("pylash.main")
SECOND = 1000


@dataclasses.dataclass()
class Geometry:
    x: int
    y: int
    width: int
    height: int


# -----------
# Application
# -----------


class PylashWallpaperApp(QWidget):

    STORE_DIR = pathlib.Path("~/Desktop/pylash").expanduser()

    def __init__(self, client: unsplash.UnsplashClient, title: str = "") -> None:
        super().__init__()
        self.client = client
        self.ctx = {}
        self._current_image: Optional[pathlib.Path] = None

        self.setup(title=title)

    def setup(self, title: str):
        self.setWindowTitle(title)
        self.addAction(self._make_close_action(callback=self.close))
        self._viewer = self._make_viewer(name="viewer", geom=(30, 30, 960, 480))
        self._nextButton = self._make_button(
            name="nextButton",
            text="下一张",
            geom=(50, 520, 400, 100),
            callback=self.next,
        )

        self._saveButton = self._make_button(
            name="saveButton",
            text="保存",
            geom=(550, 520, 400, 100),
            callback=self.save,
        )

        self._status = self._make_status_bar()
        # main window layout
        layout = self._make_layout()
        self.setLayout(layout)

    def _make_status_bar(self, css: str = ""):
        bar = QStatusBar()
        style = """
        background-color: none;
        color: 'grey';
        padding: 0;
        border: none;
        """

        if css:
            style = css
            bar.setStyleSheet(style)
        else:
            bar.setStyleSheet(style)

        ctx = self.ctx.setdefault("statusBar", {})
        ctx.update(css=textwrap.dedent(style))

        return bar

    def _make_viewer(self, name: str, geom):
        viewer = QGraphicsView()
        viewer.setObjectName(name)
        viewer.setGeometry(*geom)

        ctx = self.ctx.setdefault("viewer", {})
        ctx[name] = dict(name=name, geom=Geometry(*geom))
        return viewer

    def _make_button(self, name: str, text: str, geom, callback=None):
        btn = QPushButton(text=text)
        btn.setObjectName(name)
        btn.setGeometry(*geom)

        if callback:
            btn.clicked.connect(callback)  # noqa: ignore

        ctx = self.ctx.setdefault("button", {})
        ctx[name] = dict(
            name=name,
            text=text,
            geom=Geometry(*geom),
            callback=callback.__name__ if callback else None,
        )
        return btn

    def _make_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self._viewer)

        # button layout
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self._nextButton)
        btn_layout.addWidget(self._saveButton)

        layout.addWidget(self._status)
        layout.addLayout(btn_layout)
        return layout

    def _check_store_dir(self):
        if not self.STORE_DIR.exists():
            LOG.debug(f"initialization the directory to save a photo: {self.STORE_DIR}")
            self.STORE_DIR.mkdir()

    def _make_image_layer(self, data):
        image = QPixmap()
        image.loadFromData(data)

        scene = QGraphicsScene()
        scene.addPixmap(image)

        return scene

    @Slot()
    def save(self):
        """save photo to specific directory."""
        self._check_store_dir()  # create a directory or not before saving
        if not self._current_image:
            self._status.showMessage(
                "There isn't any image on the screen", timeout=5 * SECOND
            )
            return

        name = self._current_image.name
        fpath = self.STORE_DIR.joinpath(name)
        if fpath.exists():
            self._status.showMessage(
                f"this image has saved to {fpath}", timeout=5 * SECOND
            )
            LOG.warning(f"{fpath} image has existed.")
            return

        shutil.copy(self._current_image, fpath)
        self._status.showMessage(f"save to {fpath}")

    @Slot()
    def next(self):
        """fetch the next photo."""
        if self._status.currentMessage():
            self._status.clearMessage()

        image = self.client.fetch()
        if not image:
            msg = "the api has been limited, please try it after next hour time."
            self._status.showMessage(msg)
            LOG.warning(msg)
            return

        self._current_image = image

        scene = self._make_image_layer(data=image.read_bytes())
        self._viewer.setScene(scene)

    def _make_close_action(self, callback):
        key = "&Close"
        close = QAction(key, self)
        close.setShortcut(QKeySequence.Close)
        close.triggered.connect(callback)  # noqa: ignore

        ctx = self.ctx.setdefault("actions", {})

        ctx["close"] = dict(
            key=key,
            shortcut=str(QKeySequence.Close),
            callback=callback.__name__ if callback else None,
        )

        return close

    def _close_event(self, event: QCloseEvent):
        ctx_msg = pformat(self.ctx, compact=True)
        LOG.debug(f"context: \n{ctx_msg}")
        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        box.setWindowTitle("Quit")
        box.setText("Are you sure to close window?")
        box.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        box.setDefaultButton(QMessageBox.No)

        choice = box.exec()
        key = "No" if choice == 65536 else "Yes"
        LOG.debug(f"choice info(choice={key}, number={choice})")
        if choice == QMessageBox.No:
            event.ignore()
        else:
            event.accept()

    def closeEvent(self, event: QCloseEvent):
        self._close_event(event)


def main():
    # create application window loop.
    window = QApplication(sys.argv)

    # show content.
    client = unsplash.UnsplashClient(token=settings.TOKEN)
    app = PylashWallpaperApp(client=client, title="Unsplash 随机壁纸获取器")
    app.resize(1440, 900)
    app.show()

    # exit when application window closed.
    sys.exit(window.exec())


if __name__ == "__main__":
    main()
