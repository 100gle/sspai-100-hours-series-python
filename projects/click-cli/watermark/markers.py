from __future__ import annotations

import logging

from PIL import Image, ImageDraw, ImageFont
from watermark.helper import adjust_marker_layer, set_opacity

logger = logging.getLogger("watermark.markers")


def text_marker(
    font_or_path,
    content,
    size=20,
    color="black",
    rotation=0,
    alpha: int | float = 1,
    **kwargs,
):

    # set font and get the font size which determined by content.
    font = ImageFont.truetype(font_or_path, size=size)
    CONTENT_SIZE = font.getsize(text=content)

    layer = Image.new("RGBA", CONTENT_SIZE)

    plot = ImageDraw.Draw(layer)
    plot.text(
        xy=(0, 0),  # x=0, y=0
        text=content,
        fill=color,
        font=font,
        align="center",
    )
    if rotation:
        layer = layer.rotate(rotation, expand=True)

    if alpha:
        layer = set_opacity(layer, alpha)

    return layer


def image_marker(fpath, zoom=0.8, rotation=0, alpha: int | float = 1, **kwargs):

    # convert image watermarker to RGBA mode.
    layer = Image.open(fpath).convert("RGBA")

    width, height = layer.size

    if 0 <= zoom <= 1:
        layer = layer.resize((int(width * zoom), int(height * zoom)))

    if rotation:
        layer = layer.rotate(rotation, expand=True)

    if alpha:
        layer = set_opacity(layer, alpha)

    return layer


def make(path, *, text=None, image=None, **kwargs):
    pic = Image.open(path).convert("RGBA")
    if text and not image:
        marker = text_marker(text, **kwargs)
    elif not text and image:
        marker = image_marker(image, **kwargs)
    else:
        raise ValueError("use text or image")

    layer = adjust_marker_layer(pic, marker, **kwargs)
    marked = Image.alpha_composite(pic, layer)

    return marked
