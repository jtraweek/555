import unittest
import GedcomClass
from Sprint4 import user_story_42
from Sprint4 import user_story_34
from Sprint4 import user_story_31
from Sprint4 import user_story_38
from Sprint4 import user_story_35
from Sprint4 import user_story_36
from Sprint4 import user_story_33
from Sprint4 import user_story_39


class TestMethods4(unittest.TestCase):
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

    def test_us31(self):
        file = open('./test_ged/user_story_31_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        condition1 = user_story_31.living_singles(individuals)
        self.assertListEqual(condition1, ['I3', 'I4'])
        file.close()

    def test_us38(self):
        file = open('./test_ged/user_story_38_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        condition1 = user_story_38.upcoming_births(individuals)
        self.assertListEqual(condition1, ['I5'])
        file.close()

    def test_us35(self):
        file = open('./test_ged/user_story_35+36_test_1.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        condition1 = user_story_35.recently_born(individuals)
        self.assertEqual(condition1, ['I7', 'I8'])
        file.close()

        file = open('./test_ged/user_story_35+36_test_2.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        condition2 = user_story_35.recently_born(individuals)
        self.assertEqual(condition2, [])
        file.close()

    def test_us36(self):
        file = open('./test_ged/user_story_35+36_test_1.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        condition1 = user_story_36.recently_dead(individuals)
        self.assertEqual(condition1, ['I1', 'I6'])
        file.close()

        file = open('./test_ged/user_story_35+36_test_2.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        condition2 = user_story_35.recently_born(individuals)
        self.assertEqual(condition2, [])
        file.close()

    def test_us33(self):
        file = open('./test_ged/user_story_33_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        condition1 = user_story_33.recent_orphans(families, individuals)
        self.assertEqual(condition1, ['I3'])
        file.close()

    def test_us39(self):
        file = open('./test_ged/user_story_33_test.ged', 'r')
        families = GedcomClass.read_families(file)
        condition1 = user_story_39.upcoming_anniversaries(families)
        self.assertEqual(condition1, ['F3'])
        file.close()


if __name__ == "__main__":
    unittest.main()
