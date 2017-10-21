import unittest
import GedcomClass
from Sprint3 import user_story_13
from Sprint3 import user_story_21


class JL(unittest.TestCase):
    def test_us13(self):
        file = open('./test_ged/user_story_13_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        condition1 = user_story_13.siblings_spacing(GedcomClass.get_individual('I4', individuals),
                                                    GedcomClass.get_family('F1', families), individuals)
        self.assertEqual(condition1, True)
        condition2 = user_story_13.siblings_spacing(GedcomClass.get_individual('I5', individuals),
                                                    GedcomClass.get_family('F1', families), individuals)
        self.assertEqual(condition2, True)
        condition3 = user_story_13.siblings_spacing(GedcomClass.get_individual('I6', individuals),
                                                    GedcomClass.get_family('F1', families), individuals)
        self.assertEqual(condition3, False)
        file.close()

    def test_us21(self):
        file = open('./test_ged/user_story_21_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        condition1 = user_story_21.correct_gender(GedcomClass.get_family('F1', families), individuals)
        self.assertEqual(condition1, True)
        condition2 = user_story_21.correct_gender(GedcomClass.get_family('F2', families), individuals)
        self.assertEqual(condition2, False)
        file.close()


if __name__ == "__main__":
    unittest.main()
