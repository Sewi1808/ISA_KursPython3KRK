import unittest

from .kwiaciarnia_exercise import Kwiat
from .kwiaciarnia_exercise import Bukiet


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
        k = Bukiet("Tulip")

        self.assertIsInstance(k, Bukiet)