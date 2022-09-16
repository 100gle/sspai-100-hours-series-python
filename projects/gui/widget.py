import sys

from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        label = QLabel()
        label.setText("Hello, World!")
        label.setStyleSheet(
            """
            QLabel {
                font-size: 20px;
                text-align: center;
                margin: auto 50%;
                padding-bottom: 5px;
            }
            """
        )
        self.label = label

        editor = QLineEdit()
        editor.setPlaceholderText("input your name here.")
        editor.textChanged.connect(self.echo)
        self.editor = editor

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.editor)

        self.setLayout(layout)

    def echo(self, name: str = ""):
        if name:
            msg = f"Hello, {name}!"
        else:
            msg = f"Hello, world!"
        self.label.setText(msg)


def main():
    app = QApplication()
    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
