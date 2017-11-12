import unittest
import GedcomClass
from Sprint4 import user_story_42
from Sprint4 import user_story_34
from Sprint4 import US_31
from Sprint4 import US_41


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

    def test_us34(self):
        file = open('./test_ged/user_story_34_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)

        condition1 = user_story_34.list_large_age_differences(individuals, families)
        self.assertEqual(condition1, ['F1'])

        file.close()

class MM(unittest.TestCase):
    def test_us31(self):
        file = open('./test_ged/user_story_31_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        condition1 = US_31.living_singles(families, individuals)
        self.assertListEqual(condition1, ['I1', 'I4'])
        file.close()

    def test_us41(self):
        file = open('./test_ged/user_story_41_test_2.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        condition1 = US_41.upcoming_births(individuals)
        self.assertListEqual(condition1, ['I3', 'I4', 'I5'])
        file.close()

# class JT(unittest.TestCase):
#
# class CE(unittest.TestCase):





if __name__ == "__main__":
    unittest.main()
