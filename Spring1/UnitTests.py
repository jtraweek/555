import Gedcom
import unittest
from Spring1 import UsersStories

file = open('../Test GEDCOM Files/Liu ged.ged', 'r')
individuals = Gedcom.read_individuals(file)
families = Gedcom.read_families(file)


class TestMethods(unittest.TestCase):
    def test_f1_divorce(self):
        self.assertTrue(UsersStories.is_marriage_before_divorce('F1', families))

    def test_f1_death(self):
        self.assertFalse(UsersStories.is_marriage_before_death('I2', 'F1', families, individuals))

    def test_f2_divorce(self):
        self.assertFalse(UsersStories.is_marriage_before_divorce('F2', families))

    def test_f2_death(self):
        self.assertTrue(UsersStories.is_marriage_before_death('I4', 'F2', families, individuals))

    def test_f3_divorce(self):
        self.assertTrue(UsersStories.is_marriage_before_divorce('F3', families))

    def test_f3_death(self):
        self.assertTrue(UsersStories.is_marriage_before_death('I5', 'F3', families, individuals))

    def test_I1_dates_before_now(self):
        self.assertTrue(UsersStories.dates_b4_current_indi('18 DEC 0230'))

    def test_I7_dates_before_now(self):
        self.assertTrue(UsersStories.dates_b4_current_indi('11 OCT 0283'))

    def test_invalid_birth_before_now(self):
        self.assertFalse(UsersStories.dates_b4_current_indi('11 OCT 2020'))

    def test_invalid_death_before_now(self):
        self.assertTrue(UsersStories.dates_b4_current_indi('11 FEB 2016'))

    def test_invalid_marriage_before_now(self):
        self.assertFalse(UsersStories.dates_b4_current_fam('11 OCT 2018'))

    def test_invalid_divorce_before_now(self):
        self.assertTrue(UsersStories.dates_b4_current_fam('11 DEC 2016'))

    def test_no_death_div_b4_death(self):
        self.assertTrue(UsersStories.div_b4_death('12 NOV 2014', 'NA'))

    def test_valid_div_b4_death(self):
        self.assertTrue(UsersStories.div_b4_death('12 NOV 2014', '15 JAN 2015'))

    def test_div_after_wife_death_div_b4_death(self):
        self.assertFalse(UsersStories.div_b4_death('15 JAN 2015', '21 FEB 2013'))

    def test_div_after_husb_death_div_b4_death(self):
        self.assertFalse(UsersStories.div_b4_death('12 NOV 2014', '15 JAN 2012'))

    def test_div_after_both_death_div_b4_death(self):
        self.assertFalse(UsersStories.div_b4_death('12 NOV 2014', '15 JAN 2010'))

    def test_no_div_div_b4_death(self):
        self.assertTrue(UsersStories.div_b4_death('NA', '15 JAN 2015'))

    def test_birth_b4_death(self):  # YOU ARE TESTING THE FUNCTION, NOT THE VALUES!
        self.assertTrue(UsersStories.bir_deth('I1', individuals))
        self.assertTrue(UsersStories.bir_deth('I2', individuals))
        self.assertTrue(UsersStories.bir_deth('I3', individuals))
        self.assertFalse(UsersStories.bir_deth('I11', individuals))
        self.assertFalse(UsersStories.bir_deth('I12', individuals))

    def test_birth_b4_marriage(self):
        self.assertTrue(UsersStories.bir_marriage('I17', 'F7', individuals, families))
        self.assertTrue(UsersStories.bir_marriage('I15', 'F7', individuals, families))
        self.assertTrue(UsersStories.bir_marriage('I18', 'F8', individuals, families))
        self.assertFalse(UsersStories.bir_marriage('I19', 'F8', individuals, families))
        self.assertFalse(UsersStories.bir_marriage('I21', 'F9', individuals, families))

    def testAge(self):
        condition_satisfied_1 = UsersStories.age_less('I7', individuals)
        self.assertEqual(condition_satisfied_1, True)

        condition_satisfied_2 = UsersStories.age_less('I6', individuals)
        self.assertEqual(condition_satisfied_2, True)

        condition_satisfied_3 = UsersStories.age_less('I8', individuals)
        self.assertEqual(condition_satisfied_3, True)

        condition_satisfied_4 = UsersStories.age_less('I11', individuals)
        self.assertEqual(condition_satisfied_4, True)

        condition_satisfied_5 = UsersStories.age_less('I3', individuals)
        self.assertEqual(condition_satisfied_5, True)

    def testChildBirthAfterMarriage(self):
        condition_satisfied_1 = UsersStories.child_birth_after_marriage('15 NOV 2014', '15 JAN 2010')
        self.assertEqual(condition_satisfied_1, False)

        condition_satisfied_2 = UsersStories.child_birth_after_marriage('15 JAN 2015', '21 FEB 2013')
        self.assertEqual(condition_satisfied_2, False)

        condition_satisfied_3 = UsersStories.child_birth_after_marriage('12 NOV 2014', '15 JAN 2012')
        self.assertEqual(condition_satisfied_3, False)

        condition_satisfied_4 = UsersStories.child_birth_after_marriage('NA', '15 JAN 2015')
        self.assertEqual(condition_satisfied_4, True)

        condition_satisfied_5 = UsersStories.child_birth_after_marriage('12 NOV 2014', 'NA')
        self.assertEqual(condition_satisfied_5, True)

    def testChildBirthBeforeDivorce(self):
        condition_satisfied_1 = UsersStories.child_birth_before_divorce('15 JAN 2010', '12 NOV 2014')
        self.assertEqual(condition_satisfied_1, False)

        condition_satisfied_2 = UsersStories.child_birth_before_divorce('21 FEB 2013', '21 NOV 2015')
        self.assertEqual(condition_satisfied_2, False)

        condition_satisfied_3 = UsersStories.child_birth_before_divorce('15 JAN 2012', '15 OCT 2014')
        self.assertEqual(condition_satisfied_3, False)

        condition_satisfied_4 = UsersStories.child_birth_before_divorce('15 JAN 2016', '15 JAN 2015')
        self.assertEqual(condition_satisfied_4, True)

        condition_satisfied_5 = UsersStories.child_birth_before_divorce('12 NOV 2014', 'NA')
        self.assertEqual(condition_satisfied_5, True)


if __name__ == '__main__':
    unittest.main()
