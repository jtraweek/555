import unittest
import GedcomClass
from Sprint3 import user_story_13
from Sprint3 import user_story_21
from Sprint3 import US-29
from Sprint3 import US-30





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

class MM(unittest.TestCase):
    def test_us29(self):
        #file = open('./test_ged/user_story_13_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)

        condition1 = US-29.living_married(GedcomClass.get_individual('I4',individuals),families,individuals)
        self.assertEqual(condition1, True)

        condition2 = US-29.living_married(GedcomClass.get_individual('I3',individuals),families,individuals)
        self.assertEqual(condition2, False)
        file.close()

    def test_us30(self):
        #file = open('./test_ged/user_story_21_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)

        condition1 = US-30.deceased_people(GedcomClass.get_individual('I1',individuals),individuals)
        self.assertEqual(condition1, True)

        condition2 = US-30.deceased_people(GedcomClass.get_individual('I3',individuals),individuals)
        self.assertEqual(condition2, False)
        file.close()

if __name__ == "__main__":
    unittest.main()
