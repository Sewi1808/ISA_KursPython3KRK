import unittest

from .kwiaciarnia_exercise import Kwiat
from .kwiaciarnia_exercise import Bukiet

if __name__ == "__main__":
    unittest.main()


class TestKwiat(unittest.TestCase):

    def test_if_constructor_return_Kwiat_instance(self):
        k = Kwiat(25, "Tulip")

        self.assertIsInstance(k, Kwiat)

    def test_if_instance_has_2_attrib(self):
        k = Kwiat(25, "Tulip")

        self.assertTrue(hasattr(k, "cena"))
        self.assertTrue(hasattr(k, "rodzaj"))


class TestBukiet(unittest.TestCase):

    def test_if_constructor_return_Bukiet_instance(self):
        b = Bukiet("Tulip")

        self.assertIsInstance(b, Bukiet)

    def test_if_instance_has_attrib(self):
        b = Bukiet("Tulip")

        self.assertTrue(hasattr(b, "zbior_kwiatow"))

    def test_if_lilly_is_in_Bukiet_instance(self):
        b = Bukiet(["Tulip", "Lilly", "Rose"])

        self.assertIn('Lilly', b.zbior_kwiatow)
