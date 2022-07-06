import logging

from PIL import Image, ImageEnhance

logger = logging.getLogger("watermark.helper")


def set_opacity(layer, alpha):
    if layer.mode != "RGBA":
        layer = layer.convert("RGBA")

    if 0 <= alpha <= 1:
        alpha_layer = layer.split()[-1]
        alpha_layer = ImageEnhance.Brightness(alpha_layer).enhance(alpha)
        layer.putalpha(alpha_layer)
    else:
        logger.warning(
            f"alpha not works, because the value {alpha} not in [0, 1] interval."
        )

    return layer


def get_location(image_size, marker_size, loc, offset=0):
    img_x, img_y = image_size
    mx, my = marker_size

    half_x = int((img_x - mx) / 2)
    half_y = int((img_y - my) / 2)

    locations = {
        # top orient
        "top-left": (0, 0),
        "top": (half_x, 0),
        "top-right": (img_x - mx, 0),
        # center orient
        "center-left": (0, half_y),
        "center": (half_x, half_y),
        "center-right": (img_x - mx, half_y),
        # bottom orient
        "bottom-left": (0, img_y - my),
        "bottom": (half_x, img_y - my),
        "bottom-right": (img_x - mx, img_y - my),
    }
    location = locations[loc]
    logger.debug(
        f"image size: {image_size}, marker size: {marker_size}, {loc} default location: {location}"
    )

    if offset:
        x, y = location

        if x == 0:
            x += offset
        elif x != half_x:
            x -= offset

        if loc.startswith("top"):
            y += offset
        elif loc.startswith("bottom"):
            y -= offset

        location = (x, y)

    logger.debug(f"{loc} location: {location}")

    return location


def adjust_marker_layer(
    image,
    marker,
    loc="center",
    offset=0,
    **kwargs,
):
    layer = Image.new("RGBA", size=image.size)

    locations = [
        "top",
        "top-left",
        "top-right",
        "bottom",
        "bottom-left",
        "bottom-right",
        "center",
        "center-left",
        "center-right",
    ]

    if loc != "all":
        if loc not in locations:
            logger.warning(f"{loc} location not found, use default location: center")
            locations = ["center"]
        else:
            locations = [loc]

    for location in locations:
        position = get_location(
            image.size,
            marker.size,
            loc=location,
            offset=offset,
        )
        layer.paste(marker, position, mask=marker)

    return layer
