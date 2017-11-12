import unittest
import GedcomClass
from Sprint4 import user_story_42


class JL(unittest.TestCase):
    def test_us42(self):
        file = open('./test_ged/user_story_42_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)

        condition1 = user_story_42.is_date_valid(GedcomClass.get_individual('I1', individuals))
        self.assertFalse(condition1)
        condition2 = user_story_42.is_date_valid(GedcomClass.get_individual('I2', individuals))
        self.assertTrue(condition2)
        condition3 = user_story_42.is_date_valid(GedcomClass.get_family('F1', families))
        self.assertFalse(condition3)
        condition4 = user_story_42.is_date_valid(GedcomClass.get_family('F2', families))
        self.assertTrue(condition4)

        file.close()

class JT(unittest.TestCase):

class CE(unittest.TestCase):

class MM(unittest.TestCase):



if __name__ == "__main__":
    unittest.main()
