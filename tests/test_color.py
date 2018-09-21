from unittest import TestCase

from maki.color import Color


class ColorTest(TestCase):
    def test_is_light(self):
        self.assertTrue(Color.from_hex("#ffffff").is_light)
        self.assertTrue(Color.from_hex("#fff").is_light)
        self.assertFalse(Color.from_hex("#000").is_light)

    def test_invalid_hex(self):
        with self.assertRaises(ValueError):
            Color.from_hex("azz")

    def test_valid_hex(self):
        self.assertEqual(Color.from_hex("000").rgb, (0, 0, 0))
        self.assertEqual(Color.from_hex("aff").rgb, (170, 255, 255))

    def test_equality(self):
        self.assertEqual(Color.from_hex("#fff"), Color(255, 255, 255))
        self.assertEqual(Color.from_hex("aff"), Color.from_hex("aaffff"))

    def test_luminance(self):
        self.assertEqual(Color(0, 0, 0).luminance, 0)
        self.assertEqual(Color(255, 255, 255).luminance, 1)
