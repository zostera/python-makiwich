from unittest import TestCase

from maki import MakiMarker

import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")


class MakiMarkerTest(TestCase):
    def setUp(self):
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

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

                    with open(os.path.join(OUTPUT_DIR, fname), "w") as out:
                        out.write(marker.svg())
                    with open(os.path.join(OUTPUT_DIR, png), "wb") as out:
                        out.write(marker.png())

        with open(os.path.join(OUTPUT_DIR, "test.html"), "w") as out:
            out.write(" ".join(map(lambda x: "" if x is None else f'<img src="{x}" />', filenames)))

        MakiMarker(symbol="beer").svg()
        MakiMarker(symbol="globe").svg()
