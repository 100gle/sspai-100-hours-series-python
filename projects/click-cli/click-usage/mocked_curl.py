import click


def record_params(**kwargs):
    tmpl = ""
    for key, value in kwargs.items():
        tmpl += f"  {key}: {value}\n"
    return tmpl


@click.command()
@click.argument("url", type=str)
@click.option(
    "-X",
    "--method",
    default="GET",
    type=click.Choice(["GET", "POST"], case_sensitive=False),
    show_default=True,
    help="the HTTP method to use",
)
@click.option(
    "--data",
    default=None,
    multiple=True,
    help="data to be sent with the request",
)
@click.option(
    "-d",
    "--header",
    default=None,
    multiple=True,
    help="the request header",
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    help="verbose mode",
)
def mocked_curl(url, method, verbose=False, **kwargs):
    """request for target url"""

    default_params = dict(method=method)
    extra = {}

    data = kwargs.get("data")
    header = kwargs.get("header")
    if header:
        default_params.update(dict(header=header))

    if method == "POST":
        if data:
            extra = dict(method="POST", data=data)
        else:
            extra = dict(method="POST")

    if extra:
        default_params.update(extra)

    if verbose:
        log = record_params(**default_params)
        click.echo(f"request for {url} with: \n{log}")
        return

    click.echo(f"request for {url} ...")


if __name__ == '__main__':
    mocked_curl()
