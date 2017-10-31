import unittest
import GedcomClass
from Sprint3 import user_story_13
from Sprint3 import user_story_21
from Sprint3 import US_29
from Sprint3 import US_30
from Sprint3 import user_story_23
from Sprint3 import user_story_24
from Sprint3 import user_story_28



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
""""
class MM(unittest.TestCase):
    def test_us29(self):
        file = open('./test_ged/user_story_13_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)

        condition1 = US_29.living_married(GedcomClass.get_individual('I4',individuals),families,individuals)
        self.assertEqual(condition1, True)

        condition2 = US_29.living_married(GedcomClass.get_individual('I3',individuals),families,individuals)
        self.assertEqual(condition2, False)
        file.close()

    def test_us30(self):
        file = open('./test_ged/user_story_21_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)

        condition1 = US_30.deceased_people(GedcomClass.get_individual('I1',individuals),individuals)
        self.assertEqual(condition1, True)

        condition2 = US_30.deceased_people(GedcomClass.get_individual('I3',individuals),individuals)
        self.assertEqual(condition2, False)
        file.close()
"""
class CS(unittest.TestCase):
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

        condition1 = user_story_24.uniqueSpousesAndMarriage(GedcomClass.get_family('F1', families), families,individuals )
        self.assertEqual(condition1, False)

        condition2 = user_story_24.uniqueSpousesAndMarriage(GedcomClass.get_family('F2', families), families, individuals)
        self.assertEqual(condition2, True)

        condition3 = user_story_24.uniqueSpousesAndMarriage(GedcomClass.get_family('F3', families), families, individuals)
        self.assertEqual(condition3, False)

        file.close()
        
class JT(unittest.TestCase):
    def test_us28(self):
        file = file = open('./test_ged/user_story_28_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        
        condition1 = user_story_28.order_siblings_by_age(GedcomClass.get_family('F1', families), individuals)
        self.assertEqual(condition1, ['I5', 'I3', 'I4'])
        
        condition2= user_story_28.order_siblings_by_age(GedcomClass.get_family('F2', families), individuals)
        self.assertEqual(condition2, 'No children')

if __name__ == "__main__":
    unittest.main()
