import sys

from PySide6.QtWidgets import QApplication, QMessageBox


def main():
    app = QApplication()

    box = QMessageBox()
    box.setText("Do you attempt to close window?")

    box.setStandardButtons(box.No | box.Yes)
    box.setDefaultButton(box.Yes)
    box.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
