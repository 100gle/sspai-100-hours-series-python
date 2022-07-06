import click


@click.group()
def pip():
    ...


@pip.command(name="foo")
def install():
    click.echo("Installing...")


@pip.command(name="nonfoo")
def uninstall():
    click.echo("Uninstalling...")


if __name__ == '__main__':
    pip()
