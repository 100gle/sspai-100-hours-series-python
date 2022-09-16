import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class MyWidget(QWidget):

    counter = 0

    def __init__(self) -> None:
        super().__init__()
        self.resize(200, 100)

        btn = QPushButton()
        btn.setText("Click me")
        btn.clicked.connect(self.count)
        self.btn = btn

        bar = QStatusBar()
        self.bar = bar

        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.bar)
        self.setLayout(layout)

    @Slot()
    def count(self):
        self.counter += 1
        self.bar.showMessage(f"you have clicked: {self.counter}")


def main():
    app = QApplication()
    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
