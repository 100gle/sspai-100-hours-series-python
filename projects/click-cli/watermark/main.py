import logging
import pathlib

import click
from watermark.markers import make

ImagePath = click.Path(exists=True, allow_dash=True, dir_okay=False)


def ensure_logger(level):
    logging.basicConfig(
        level=level,
        format="[{asctime}] [{levelname}] [{name}] - {message}",
        style="{",
    )


logger = logging.getLogger("watermark.cli")

COMMON_OPTIONS = [
    click.option(
        "--alpha",
        type=click.FloatRange(0.0, 1.0),
        help="the alpha value",
        show_default=True,
    ),
    click.option(
        "--rotation",
        type=int,
        default=0,
        help="the rotation value",
        show_default=True,
    ),
    click.option(
        "--offset",
        type=int,
        default=30,
        help="the offset value",
        show_default=True,
    ),
    click.option(
        "--location",
        "loc",
        type=click.Choice(
            [
                "top-left",
                "top",
                "top-right",
                "center-left",
                "center",
                "center-right",
                "bottom-left",
                "bottom",
                "bottom-right",
                "all",
            ]
        ),
        default="bottom-right",
        help="""\
        the location value,
        text watermark will be placed at the all locations if set "all" option.
        """,
        show_default=True,
    ),
    click.option(
        "-v",
        "--verbose",
        is_flag=True,
        default=False,
        help="show debug info",
        show_default=True,
    ),
]


def shared_options(func):
    for option in COMMON_OPTIONS[::-1]:
        func = option(func)
    return func


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx: click.Context, **kwargs):
    r"""the watermark cli tools implemented by 100gle."""
    if not ctx.invoked_subcommand:
        banner()


def banner():
    msg = r"""
 _       __        __                                       __
| |     / /____ _ / /_ ___   _____ ____ ___   ____ _ _____ / /__
| | /| / // __ `// __// _ \ / ___// __ `__ \ / __ `// ___// //_/
| |/ |/ // /_/ // /_ /  __// /   / / / / / // /_/ // /   / ,<
|__/|__/ \__,_/ \__/ \___//_/   /_/ /_/ /_/ \__,_//_/   /_/|_|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Hope you enjoy it.
You can use this command to get help:

    $ watermark -h
"""
    click.echo(msg)


@cli.command()
@click.argument("content")
@click.argument("path", type=ImagePath)
@click.option(
    "-f",
    "--font-name",
    "font",
    type=str,
    help="the font name value",
)
@click.option(
    "-F",
    "--font-path",
    type=ImagePath,
    help="the font path if font name isn't passed.",
)
@click.option(
    "-s",
    "--font-size",
    "size",
    type=int,
    default=20,
    help="the font size value",
    show_default=True,
)
@click.option(
    "--color",
    type=str,
    default="black",
    help="""\
    the color value,
    you can use hex color code like "#000000" or color name "black".
    """,
    show_default=True,
)
@shared_options
def text(path, font, font_path, **kwargs):
    """the sub-command for text watermark."""
    verbose = kwargs.get("verbose")
    if verbose:
        ensure_logger(level=logging.DEBUG)
        logger.debug("enable verbose mode.")

    font_or_path = font or font_path
    logger.debug(f"image watermark options are: {kwargs}")

    fpath = pathlib.Path(path)

    name = fpath.stem
    ext = fpath.suffix
    image_suffixes = {".jpg", ".jpeg", ".png"}
    if ext not in image_suffixes:
        click.echo(f"[WARNING] can't handle {ext} image type.")
        exit(1)

    marked = make(path=path, text=font_or_path, **kwargs)
    file = fpath.parent.joinpath(f"{name}_marked{ext}")

    marked.save(file, quality=95)

    logger.debug(f"add watermark to {path} success. see {file}")


@cli.command()
@click.argument("path", type=ImagePath)
@click.option(
    "--image-watermark-path",
    "image_path",
    type=ImagePath,
    help="the path of image watermark",
)
@click.option(
    "--zoom",
    type=float,
    default=0.5,
    help="the zoom value",
    show_default=True,
)
@shared_options
def image(path, image_path, **kwargs):
    """the sub-command for image watermark."""
    verbose = kwargs.pop("verbose")
    if verbose:
        ensure_logger(level=logging.DEBUG)
        logger.debug("enable verbose mode.")

    logger.debug(f"image watermark options are: {kwargs}")
    fpath = pathlib.Path(path)

    name = fpath.stem
    ext = fpath.suffix
    image_suffixes = {".jpg", ".jpeg", ".png"}
    if ext not in image_suffixes:
        click.echo(f"[WARNING] can't handle {ext} image type.")
        exit(1)

    marked = make(path=path, image=image_path, **kwargs)
    file = fpath.parent.joinpath(f"{name}_marked{ext}")

    marked.save(file, quality=95)

    logger.debug(f"add watermark to {path} success. see {file}")


if __name__ == "__main__":
    cli()
