from unittest import TestCase

from maki import MakiMarker


class MakiMarkerTest(TestCase):
    def test_marker(self):
        filenames = []
        for size in "sl":
            for symbol in ["beer", "airfield", "park", "park-alt1", "music"]:
                filenames.append(None)
                for tint in ["3388ff", "800080", "888", "000080", "fefefe"]:
                    fname = f"test-{size}-{symbol}-{tint}.svg"
                    png = f"test-{size}-{symbol}-{tint}.png"
                    filenames.append(fname)
                    marker = MakiMarker(size=size, tint=tint, symbol=symbol)
                    open(fname, "w").write(marker.svg())
                    open(png, "wb").write(marker.png())

        open("test.html", "w").write(
            " ".join(map(lambda x: "" if x is None else f'<img src="{x}" />', filenames))
        )

        MakiMarker(symbol="beer").svg()
        MakiMarker(symbol="globe").svg()
