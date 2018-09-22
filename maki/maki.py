import os
from functools import lru_cache

import xmltodict

from .color import Color

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@lru_cache()
def svg_dict(name):
    """
    Turn a svg into a dict structure, and cache requests.
    """
    filename = os.path.join(BASE_DIR, "img", name)
    with open(filename) as svg:
        return xmltodict.parse(svg.read())


DEFAULT_BLACK = "#000"
DEFAULT_WHITE = "#fff"


class MakiMarker(object):
    """
    Generate SVG/PNG files for Maki markers to use with web mapping libraries.

    argument:
        tint (str): Any hex string to change the background color for the marker.
        symbol (str): Name of a Maki icon, defaults to a filled circle.
        size (str): "l" or "s" for large or small markers.

    Example:

        >>> from maki import MakiMarker
        >>> marker = MakiMarker(symbol="park", tint="#3388ff")
        >>> marker.svg()
        '<?xml version=...'

    """
    def __init__(self, tint="#000", symbol=None, size="l"):
        self.tint = tint
        self.size = "large" if size == "l" else "small"
        self.symbol = symbol

    def background_marker(self):
        return svg_dict(f"marker-{self.size}.svg").copy()

    def maki_icon(self):
        size = 11 if self.size == "small" else 15
        symbol = os.path.join("icons", f"{self.symbol}-{size}.svg")
        return svg_dict(symbol).copy()

    def svg(self):
        marker = self.background_marker()
        basepaths = marker["svg"]["g"]["g"]["g"]

        if self.symbol:
            try:
                icon = self.maki_icon()["svg"]["path"]
                basepaths[3]["path"] = {"@id": "icon", "@d": icon["@d"]}
            except KeyError as e:
                # some icons have a <g>-tag containing paths. They seem to need a slightly different
                # treatment.
                icon = self.maki_icon()["svg"]["g"]
                basepaths[3] = {"@id": "maki", "g": icon["g"], "@transform": "translate(6, 7)"}

            try:
                basepaths.remove(basepaths[4])
            except IndexError:
                pass

            # move single-char svg's to the center
            if len(self.symbol) == 1:
                x, y = (9, 7) if self.size == "small" else (10, 8)
                basepaths[3]["@transform"] = f"translate(x, y)"

        color = Color.from_hex(self.tint)
        # Change the tint on the marker background
        basepaths[1]["@fill"] = color.hex
        # Swap the border color if the tint is light and there is a symbol
        basepaths[2]["@fill"] = color.most_readable().hex

        # Some Maki icons have different SVG makeups. This attempts to apply the tint to the correct path
        foreground_color = DEFAULT_BLACK if color.is_light else DEFAULT_WHITE
        if "path" in basepaths[3]:
            # If the background color is light, apply a light tint to the icon or text to make it stand out more
            basepaths[3]["path"]["@style"] = f"fill:{foreground_color}"
        else:
            basepaths[3]["@fill"] = foreground_color

        # marker["svg"]["g"]["g"]["g"] = basepaths
        return xmltodict.unparse(marker)

    def png(self, **kwargs):
        import cairosvg

        return cairosvg.svg2png(bytestring=self.svg().encode(), **kwargs)
