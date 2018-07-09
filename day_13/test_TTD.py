import unittest

from .person import Person


class TestPerson(unittest.TestCase):
    def test_if_person_exist(self):
        p = Person()

        self.assertIsInstance(p, Person)

    def test_if_person_has_name_and_surname(self):
        p = Person()

        self.assertTrue(hasattr(p, 'name'))
        self.assertTrue(hasattr(p, 'surname'))

    def test_if_person_name_and_surname_is_real(self):
        p = Person()

        self.assertEqual(p.name, 'Jan')
        self.assertEqual(p.surname, 'Kowalski')