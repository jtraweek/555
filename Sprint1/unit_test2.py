import GedcomClass
import unittest
from Sprint1 import user_story_2

file = open('../Test GEDCOM Files/Liu ged.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)


class TestMethods(unittest.TestCase):
    def test_birth_b4_marriage(self):
        self.assertTrue(user_story_2.bir_marriage('I17', 'F7','25 SEP 1928','10 JAN'))
        self.assertFalse(user_story_2.bir_marriage('I15', 'F7','21 NOV 1924','1 JAN 1800'))
        self.assertTrue(user_story_2.bir_marriage('I18', 'F8','NA' ,' '))

if __name__ == '__main__':
    unittest.main()
