import unittest
from datetime import datetime
from Sprint2 import us14
from Sprint2 import us15
from Sprint2 import us16
from Sprint2 import us22
from Sprint2 import user_story_10
from Sprint2 import user_story_11
import GedcomClass


class JL(unittest.TestCase):
    def test_us14(self):
        file = open('./us14_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        condition1 = us14.has_more_than_five_birth('F1', individuals, families)
        self.assertEqual(condition1, True)
        condition2 = us14.has_more_than_five_birth('F2', individuals, families)
        self.assertEqual(condition2, False)
        file.close()

    def test_us15(self):
        file = open('./us15_test.ged', 'r')
        families = GedcomClass.read_families(file)
        condition1 = us15.has_more_than_fifteen_siblings('F1', families)
        self.assertEqual(condition1, True)
        condition2 = us15.has_more_than_fifteen_siblings('F2', families)
        self.assertEqual(condition2, False)
        file.close()

    def test_us16(self):
        file = open('./us16_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        condition1 = us16.same_male_last_name('F1', individuals, families)
        self.assertEqual(condition1, False)
        condition2 = us16.same_male_last_name('F2', individuals, families)
        self.assertEqual(condition2, True)
        file.close()

    def test_us22(self):
        file = open('./us22_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        condition1 = us22.is_id_unique('I1', individuals)
        self.assertEqual(condition1, True)
        condition2 = us22.is_id_unique('I3', individuals)
        self.assertEqual(condition2, False)
        condition3 = us22.is_id_unique('F2', families)
        self.assertEqual(condition3, True)
        condition4 = us22.is_id_unique('F1', families)
        self.assertEqual(condition4, False)
        file.close()


class JT(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
