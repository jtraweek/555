import unittest
import Gedcom
from Spring1 import UserStory45

file = open('../Test GEDCOM Files/Liu ged.ged', 'r')
individuals = Gedcom.read_individuals(file)
families = Gedcom.read_families(file)


class TestMethods(unittest.TestCase):
    def test_f1_divorce(self):
        self.assertTrue(UserStory45.is_marriage_before_divorce('F1', families))

    def test_f1_death(self):
        self.assertFalse(UserStory45.is_marriage_before_death('F1', families, individuals))

    def test_f2_divorce(self):
        self.assertFalse(UserStory45.is_marriage_before_divorce('F2', families))

    def test_f2_death(self):
        self.assertTrue(UserStory45.is_marriage_before_death('F2', families, individuals))

    def test_f3_divorce(self):
        self.assertTrue(UserStory45.is_marriage_before_divorce('F3', families))

    def test_f3_death(self):
        self.assertTrue(UserStory45.is_marriage_before_death('F3', families, individuals))
