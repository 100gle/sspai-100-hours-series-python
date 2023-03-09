import re
from textwrap import dedent

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Footer, Header, Static

lorem = """\
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed eget suscipit ligula.
Curabitur id justo imperdiet, pretium orci sed, tempus leo.
Integer vulputate vitae diam efficitur tempus.
Donec vel est ac purus feugiat ultricies sit amet non sapien.
Vivamus faucibus viverra bibendum.
Integer congue sed mi et imperdiet. Praesent quis dapibus neque.
Cras arcu purus, laoreet eu nibh scelerisque, bibendum tincidunt mauris.
Cras congue erat leo, non efficitur tellus auctor a.
"""


class LoremWidget(Static):

    is_highlight = reactive(False, layout=True)
    _RE_LOREM = re.compile("(?P<target>Lorem ipsum)", re.I)

    _cache_lorem = None
    _raw_lorem = dedent(lorem)

    def on_mount(self) -> None:
        self.update(self._raw_lorem)

    async def watch_is_highlight(self, old_value, new_value) -> None:
        if self.is_highlight:
            content = self.marked_lorem()
            self.update(content)
        else:
            self.update(self._raw_lorem)

    def marked_lorem(self):
        if self._cache_lorem:
            return self._cache_lorem

        content = self._RE_LOREM.sub(r"[u red b]\1[/]", lorem)
        self._cache_lorem = content
        return content


class SimpleApp(App):
    BINDINGS = [
        ("h", "highlight", "Highlight lorem"),
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(LoremWidget(id="lorem"))
        yield Footer()

    def action_highlight(self) -> None:
        widget = self.query_one("#lorem")
        widget.is_highlight = not widget.is_highlight

    def action_quit(self) -> None:
        self.exit(0)


if __name__ == '__main__':
    app = SimpleApp()
    app.run()
