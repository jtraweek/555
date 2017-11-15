import unittest
from datetime import datetime
from Sprint2 import user_story_14
from Sprint2 import user_story_15
from Sprint2 import user_story_16
from Sprint2 import user_story_22
from Sprint2 import user_story_09
from Sprint2 import user_story_10
from Sprint2 import user_story_11
from Sprint2 import user_story_12
import GedcomClass


class TestMethods2(unittest.TestCase):
    def test_us14(self):
        file = open('./test_ged/user_story_14_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        condition1 = user_story_14.has_more_than_five_birth('F1', individuals, families)
        self.assertEqual(condition1, True)
        condition2 = user_story_14.has_more_than_five_birth('F2', individuals, families)
        self.assertEqual(condition2, False)
        file.close()

    def test_us15(self):
        file = open('./test_ged/user_story_15_test.ged', 'r')
        families = GedcomClass.read_families(file)
        condition1 = user_story_15.has_more_than_fifteen_siblings('F1', families)
        self.assertEqual(condition1, True)
        condition2 = user_story_15.has_more_than_fifteen_siblings('F2', families)
        self.assertEqual(condition2, False)
        file.close()

    def test_us16(self):
        file = open('./test_ged/user_story_16_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        condition1 = user_story_16.same_male_last_name('F1', individuals, families)
        self.assertEqual(condition1, False)
        condition2 = user_story_16.same_male_last_name('F2', individuals, families)
        self.assertEqual(condition2, True)
        file.close()

    def test_us22(self):
        file = open('./test_ged/user_story_22_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        condition1 = user_story_22.is_id_unique('I1', individuals)
        self.assertEqual(condition1, True)
        condition2 = user_story_22.is_id_unique('I3', individuals)
        self.assertEqual(condition2, False)
        condition3 = user_story_22.is_id_unique('F2', families)
        self.assertEqual(condition3, True)
        condition4 = user_story_22.is_id_unique('F1', families)
        self.assertEqual(condition4, False)
        file.close()



    def test_us10(self):
        birthday = datetime.strptime('29 AUG 1993', '%d %b %Y')
        marriage_ok = datetime.strptime('30 OCT 2018', '%d %b %Y')
        marriage_not_ok = datetime.strptime('12 DEC 2006', '%d %b %Y')
        self.assertTrue(user_story_10.marriage_after_14(birthday.date(), marriage_ok.date()))
        self.assertFalse(user_story_10.marriage_after_14(birthday.date(), marriage_not_ok.date()))
        self.assertEqual(user_story_10.marriage_after_14(birthday.date(), 'NA'), 'Not married')

    def test_us11(self):
        file = open('../Test GEDCOM Files/JULIE GEDCOM.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        self.assertTrue(user_story_11.no_bigamy('I1', individuals, families))
        self.assertTrue(user_story_11.no_bigamy('I11', individuals, families))
        self.assertTrue(user_story_11.no_bigamy('I14', individuals, families))
        self.assertFalse(user_story_11.no_bigamy('I8', individuals, families))
        file.close()


    def test_us09(self):
        file = open('./test_ged/user_story_9_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        self.assertTrue(user_story_09.birth_before_parents_death('I1', individuals, families))
        self.assertTrue(user_story_09.birth_before_parents_death('I4', individuals, families))
        self.assertTrue(user_story_09.birth_before_parents_death('I5', individuals, families))
        self.assertFalse(user_story_09.birth_before_parents_death('I3', individuals, families))
        file.close()

    def test_us12(self):
        file = open('./test_ged/user_story_12_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        self.assertTrue(user_story_12.parents_not_too_old('I1', individuals, families))
        self.assertFalse(user_story_12.parents_not_too_old('I3', individuals, families))
        self.assertFalse(user_story_12.parents_not_too_old('I4', individuals, families))
        self.assertTrue(user_story_12.parents_not_too_old('I5', individuals, families))
        file.close()


'''if __name__ == "__main__":
    unittest.main()'''


