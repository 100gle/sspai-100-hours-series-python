import click


@click.group()
def pip():
    pass


@pip.command()
def install():
    """pip install method"""
    click.echo("Installing...")


@pip.command()
def uninstall():
    """pip uninstall method"""
    click.echo("Uninstalling...")


@click.group()
def pytest():
    pass


@pytest.command()
def test():
    """run the tests."""
    click.echo("Running tests...")


cli = click.CommandCollection(
    sources=[pip, pytest],
    help="the collections of custom commands",
)

if __name__ == '__main__':
    cli()
