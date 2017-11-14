import GedcomClass
import unittest
from Sprint1 import user_story_1
from Sprint1 import user_story_2
from Sprint1 import user_story_3
from Sprint1 import user_story_4
from Sprint1 import user_story_5
from Sprint1 import user_story_6
from Sprint1 import user_story_7
from Sprint1 import user_story_8


class TestMethods(unittest.TestCase):
    def test_us1(self):
        file = open('./test_ged/user_story_1_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        self.assertTrue(user_story_1.dates_b4_current_indi(individuals.get('I1').birt))
        self.assertFalse(user_story_1.dates_b4_current_indi(individuals.get('I3').birt))
        file.close()

    def test_us2(self):
        file = open('./test_ged/user_story_2_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        self.assertTrue(user_story_2.bir_marriage(individuals.get('I2'), families.get('F1')))
        self.assertFalse(user_story_2.bir_marriage(individuals.get('I1'), families.get('F1')))
        file.close()

    def test_us3(self):
        file = open('./test_ged/user_story_3_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        self.assertTrue(user_story_3.bir_deth(individuals.get('I2')))
        self.assertFalse(user_story_3.bir_deth(individuals.get('I1')))
        file.close()

    def test_us4(self):
        file = open('./test_ged/user_story_4_test.ged', 'r')
        families = GedcomClass.read_families(file)
        self.assertTrue(user_story_4.is_marriage_before_divorce(families.get('F2')))
        self.assertFalse(user_story_4.is_marriage_before_divorce(families.get('F1')))
        file.close()

    def test_us5(self):
        file = open('./test_ged/user_story_5_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        self.assertTrue(user_story_5.is_marriage_before_death(individuals.get('I2'), families.get('F1')))
        self.assertFalse(user_story_5.is_marriage_before_death(individuals.get('I1'), families.get('F1')))
        file.close()

    def test_us6(self):
        file = open('./test_ged/user_story_6_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        self.assertTrue(user_story_6.div_b4_death(individuals.get('I2'), families.get('F1')))
        self.assertFalse(user_story_6.div_b4_death(individuals.get('I1'), families.get('F1')))
        file.close()

    def test_us7(self):
        file = open('./test_ged/user_story_7_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        self.assertTrue(user_story_7.age_not_too_old(individuals.get('I2')))
        self.assertFalse(user_story_7.age_not_too_old(individuals.get('I1')))
        file.close()

    def test_us8(self):
        file = open('./test_ged/user_story_8_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        self.assertTrue(user_story_8.birth_before_marriage(individuals.get('I5'), families.get('F1')))
        self.assertFalse(user_story_8.birth_before_marriage(individuals.get('I3'), families.get('F1')))
        file.close()


'''if __name__ == '__main__':
    unittest.main()'''

