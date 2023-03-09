from textual import events
from textual.app import App
from textual.containers import Container
from textual.widgets import Static


class ClickableColorBlock(Static):
    background_toggled = False
    raw_background = ""

    def on_mount(self):
        self.styles.border = ("heavy", "white")
        self.raw_background = self.styles.background

    def on_click(self, event: events.Click):
        event.prevent_default()

        self.background_toggled = not self.background_toggled
        self.styles.background = (
            str(self.render()) if self.background_toggled else self.raw_background
        )

        self.log("block background changed!")


class DisplayApp(App):
    CSS_PATH = "css/events.css"
    background_toggled = False

    def compose(self):
        yield Container(
            ClickableColorBlock("red", classes="block"),
            ClickableColorBlock("blue", classes="block"),
            ClickableColorBlock("green", classes="block"),
            ClickableColorBlock("cyan", classes="block"),
            id="display-container",
        )

    def on_click(self):
        self.background_toggled = not self.background_toggled
        target = self.query_one("#display-container")
        blocks = target.query(".block")
        background = None
        border = None

        if self.background_toggled:
            background = "white"
            border = ("heavy", "black")
        else:
            background = "grey"
            border = ("heavy", "white")

        target.styles.background = background
        for block in blocks:
            block.styles.border = border

        self.log("container background changed!")


if __name__ == '__main__':
    app = DisplayApp()
    app.run()
