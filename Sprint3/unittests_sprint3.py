import unittest
import GedcomClass
from Sprint3 import user_story_13
from Sprint3 import user_story_21
from Sprint3 import user_story_30
from Sprint3 import user_story_29
from Sprint3 import user_story_23
from Sprint3 import user_story_24
from Sprint3 import user_story_18
from Sprint3 import user_story_28


class TestMethods3(unittest.TestCase):
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

    def test_us30(self):
        file = open('./test_ged/user_story_30_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        condition1 = user_story_30.living_married(families, individuals)
        self.assertListEqual(condition1, ['I1', 'I2'])
        file.close()

    def test_us29(self):
        file = open('./test_ged/user_story_29_test_2.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        condition1 = user_story_29.deceased_people(individuals)
        self.assertListEqual(condition1, ['I1', 'I2', 'I3', 'I4', 'I5'])
        file.close()

    def test_us23(self):
        file = open('./test_ged/user_story_23_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)

        condition1 = user_story_23.uniqueNameAndBirth(GedcomClass.get_individual('I1', individuals), individuals)
        self.assertEqual(condition1, False)

        condition2 = user_story_23.uniqueNameAndBirth(GedcomClass.get_individual('I3', individuals), individuals)
        self.assertEqual(condition2, True)

        condition3 = user_story_23.uniqueNameAndBirth(GedcomClass.get_individual('I7', individuals), individuals)
        self.assertEqual(condition3, False)

        file.close()

    def test_us24(self):
        file = open('./test_ged/user_story_24_test.ged', 'r')
        families = GedcomClass.read_families(file)
        individuals = GedcomClass.read_individuals(file)

        condition1 = user_story_24.uniqueSpousesAndMarriage(GedcomClass.get_family('F1', families), families,
                                                            individuals)
        self.assertEqual(condition1, False)

        condition2 = user_story_24.uniqueSpousesAndMarriage(GedcomClass.get_family('F2', families), families,
                                                            individuals)
        self.assertEqual(condition2, True)

        condition3 = user_story_24.uniqueSpousesAndMarriage(GedcomClass.get_family('F3', families), families,
                                                            individuals)
        self.assertEqual(condition3, False)

        file.close()

    def test_us28(self):
        file = open('./test_ged/user_story_28_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)

        condition1 = user_story_28.order_siblings_by_age(GedcomClass.get_family('F1', families), individuals)
        self.assertEqual(condition1, ['I5', 'I3', 'I4'])

        condition2 = user_story_28.order_siblings_by_age(GedcomClass.get_family('F2', families), individuals)
        self.assertEqual(condition2, 'No children')

        condition3 = user_story_28.order_siblings_by_age(GedcomClass.get_family('F3', families), individuals)
        self.assertEqual(condition3, 'Only one child')

        file.close()

    def test_us18(self):
        file = open('./test_ged/user_story_18_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)

        condition1 = user_story_18.siblings_not_married(GedcomClass.get_family('F1', families), individuals)
        self.assertEqual(condition1, True)

        condition2 = user_story_18.siblings_not_married(GedcomClass.get_family('F2', families), individuals)
        self.assertEqual(condition2, False)

        file.close()


if __name__ == "__main__":
    unittest.main()
