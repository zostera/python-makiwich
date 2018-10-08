from unittest import TestCase

from django.conf import settings
from django.http import Http404

from maki.contrib.django import maki_icon

settings.configure()


class DjangoViewTest(TestCase):
    def test_view(self):
        valid = [
            "pin-s-beer+fff.png",
            "pin-s-beer+f0f.png",
            "pin-l-park+3388ff.png",
            "pin-l-park-alt1+3388ff.png",
            "pin-l-park-alt1+3388ff@2x.png",
            "pin-l-park.png",
            "pin-l.png",
            "pin-l@2x.png",
            "pin-l.svg",
        ]
        for name in valid:
            response = maki_icon({}, name)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response["Content-Type"], "image/png" if name.endswith(".png") else "image/svg+xml"
            )

    def test_invalid(self):
        invalid = [
            ("pin-l-park-alt1+3388ff@2x.svg", "@2x suffix only valid for png."),
            ("pin-m.png", "Marker name must start with pin-s or pin-l"),
            ("pin-l.jpg", "Format must be png or svg"),
            ("pin-l-mail.png", "Symbol 'mail' does not exist"),
        ]

        for name, expected_msg in invalid:
            with self.assertRaisesRegex(Http404, expected_msg) as ex:
                maki_icon({}, name)

            self.assertEqual(str(ex.exception), expected_msg)
