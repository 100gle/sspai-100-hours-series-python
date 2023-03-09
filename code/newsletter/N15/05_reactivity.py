from textual.app import App
from textual.containers import Vertical
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Input


class WelcomeWidget(Widget):
    who = reactive("World!")
    total = reactive(15)

    def on_mount(self):
        default_styles = """
        margin: 1;
        padding: 1;
        """
        self.set_styles(default_styles)

    def render(self):
        return f":partying_face: Hello, [b red]{self.who}[/]! ({self.total}/15)"

    def watch_who(self, old_value, new_value):
        self.log(
            f"who attribute changed: old value: {old_value}, "
            f"new value: {new_value}  "
        )

    def compute_total(self):
        return len(self.who)


class InputChangeApp(App):
    def compose(self):
        yield Vertical(
            Input(placeholder="enter your name..."),
            WelcomeWidget(classes="welcome"),
        )

    def on_input_changed(self, event: Input.Changed) -> None:
        target = self.query_one(".welcome")
        value = event.value

        if len(value) > 15:
            event.input.value = value[:15]
            return

        if not value:
            target.who = "World!"
        else:
            target.who = value


if __name__ == '__main__':
    app = InputChangeApp()
    app.run()
