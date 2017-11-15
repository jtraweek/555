import GedcomClass
import unittest
from datetime import datetime
from Sprint1 import user_story_1
from Sprint1 import user_story_2
from Sprint1 import user_story_3
from Sprint1 import user_story_4
from Sprint1 import user_story_5
from Sprint1 import user_story_6
from Sprint1 import user_story_7
from Sprint1 import user_story_8
from Sprint2 import user_story_14
from Sprint2 import user_story_15
from Sprint2 import user_story_16
from Sprint2 import user_story_22
from Sprint2 import user_story_09
from Sprint2 import user_story_10
from Sprint2 import user_story_11
from Sprint2 import user_story_12
from Sprint3 import user_story_13
from Sprint3 import user_story_21
from Sprint3 import US_30
from Sprint3 import US_29
from Sprint3 import user_story_23
from Sprint3 import user_story_24
from Sprint3 import user_story_18
from Sprint3 import user_story_28
from Sprint4 import user_story_42
from Sprint4 import user_story_34
from Sprint4 import US_31
from Sprint4 import US_38
from Sprint4 import user_story_35
from Sprint4 import user_story_36
from Sprint4 import user_story_33
from Sprint4 import user_story_39

class TestMethods(unittest.TestCase):
    def test_us1(self):
        file = open('./Sprint1/test_ged/user_story_1_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        self.assertTrue(user_story_1.dates_b4_current_indi(individuals.get('I1').birt))
        self.assertFalse(user_story_1.dates_b4_current_indi(individuals.get('I3').birt))
        file.close()

    def test_us2(self):
        file = open('./Sprint1/test_ged/user_story_2_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        self.assertTrue(user_story_2.bir_marriage(individuals.get('I2'), families.get('F1')))
        self.assertFalse(user_story_2.bir_marriage(individuals.get('I1'), families.get('F1')))
        file.close()

    def test_us3(self):
        file = open('./Sprint1/test_ged/user_story_3_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        self.assertTrue(user_story_3.bir_deth(individuals.get('I2')))
        self.assertFalse(user_story_3.bir_deth(individuals.get('I1')))
        file.close()

    def test_us4(self):
        file = open('./Sprint1/test_ged/user_story_4_test.ged', 'r')
        families = GedcomClass.read_families(file)
        self.assertTrue(user_story_4.is_marriage_before_divorce(families.get('F2')))
        self.assertFalse(user_story_4.is_marriage_before_divorce(families.get('F1')))
        file.close()

    def test_us5(self):
        file = open('./Sprint1/test_ged/user_story_5_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        self.assertTrue(user_story_5.is_marriage_before_death(individuals.get('I2'), families.get('F1')))
        self.assertFalse(user_story_5.is_marriage_before_death(individuals.get('I1'), families.get('F1')))
        file.close()

    def test_us6(self):
        file = open('./Sprint1/test_ged/user_story_6_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        self.assertTrue(user_story_6.div_b4_death(individuals.get('I2'), families.get('F1')))
        self.assertFalse(user_story_6.div_b4_death(individuals.get('I1'), families.get('F1')))
        file.close()

    def test_us7(self):
        file = open('./Sprint1/test_ged/user_story_7_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        self.assertTrue(user_story_7.age_not_too_old(individuals.get('I2')))
        self.assertFalse(user_story_7.age_not_too_old(individuals.get('I1')))
        file.close()

    def test_us8(self):
        file = open('./Sprint1/test_ged/user_story_8_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        self.assertTrue(user_story_8.birth_before_marriage(individuals.get('I5'), families.get('F1')))
        self.assertFalse(user_story_8.birth_before_marriage(individuals.get('I3'), families.get('F1')))
        file.close()

class TestMethods2(unittest.TestCase):
    def test_us14(self):
        file = open('./Sprint2/test_ged/user_story_14_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        condition1 = user_story_14.has_more_than_five_birth('F1', individuals, families)
        self.assertEqual(condition1, True)
        condition2 = user_story_14.has_more_than_five_birth('F2', individuals, families)
        self.assertEqual(condition2, False)
        file.close()

    def test_us15(self):
        file = open('./Sprint2/test_ged/user_story_15_test.ged', 'r')
        families = GedcomClass.read_families(file)
        condition1 = user_story_15.has_more_than_fifteen_siblings('F1', families)
        self.assertEqual(condition1, True)
        condition2 = user_story_15.has_more_than_fifteen_siblings('F2', families)
        self.assertEqual(condition2, False)
        file.close()

    def test_us16(self):
        file = open('./Sprint2/test_ged/user_story_16_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        condition1 = user_story_16.same_male_last_name('F1', individuals, families)
        self.assertEqual(condition1, False)
        condition2 = user_story_16.same_male_last_name('F2', individuals, families)
        self.assertEqual(condition2, True)
        file.close()

    def test_us22(self):
        file = open('./Sprint2/test_ged/user_story_22_test.ged', 'r')
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
        file = open('../555/Test GEDCOM Files/JULIE GEDCOM.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        self.assertTrue(user_story_11.no_bigamy('I1', individuals, families))
        self.assertTrue(user_story_11.no_bigamy('I11', individuals, families))
        self.assertTrue(user_story_11.no_bigamy('I14', individuals, families))
        self.assertFalse(user_story_11.no_bigamy('I8', individuals, families))
        file.close()


    def test_us09(self):
        file = open('./Sprint2/test_ged/user_story_9_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        self.assertTrue(user_story_09.birth_before_parents_death('I1', individuals, families))
        self.assertTrue(user_story_09.birth_before_parents_death('I4', individuals, families))
        self.assertTrue(user_story_09.birth_before_parents_death('I5', individuals, families))
        self.assertFalse(user_story_09.birth_before_parents_death('I3', individuals, families))
        file.close()

    def test_us12(self):
        file = open('./Sprint2/test_ged/user_story_12_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        self.assertTrue(user_story_12.parents_not_too_old('I1', individuals, families))
        self.assertFalse(user_story_12.parents_not_too_old('I3', individuals, families))
        self.assertFalse(user_story_12.parents_not_too_old('I4', individuals, families))
        self.assertTrue(user_story_12.parents_not_too_old('I5', individuals, families))
        file.close()

class TestMethods3(unittest.TestCase):
    def test_us13(self):
        file = open('./Sprint3/test_ged/user_story_13_test.ged', 'r')
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
        file = open('./Sprint3/test_ged/user_story_21_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        condition1 = user_story_21.correct_gender(GedcomClass.get_family('F1', families), individuals)
        self.assertEqual(condition1, True)
        condition2 = user_story_21.correct_gender(GedcomClass.get_family('F2', families), individuals)
        self.assertEqual(condition2, False)
        file.close()


    def test_us30(self):
        file = open('./Sprint3/test_ged/user_story_30_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        condition1 = US_30.living_married(families, individuals)
        self.assertListEqual(condition1, ['I1', 'I2'])
        file.close()

    def test_us29(self):
        file = open('./Sprint3/test_ged/user_story_29_test_2.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        condition1 = US_29.deceased_people(individuals)
        self.assertListEqual(condition1, ['I1', 'I2', 'I3', 'I4', 'I5'])
        file.close()


    def test_us23(self):
        file = open('./Sprint3/test_ged/user_story_23_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)

        condition1 = user_story_23.uniqueNameAndBirth(GedcomClass.get_individual('I1', individuals), individuals)
        self.assertEqual(condition1, False)

        condition2 = user_story_23.uniqueNameAndBirth(GedcomClass.get_individual('I3', individuals), individuals)
        self.assertEqual(condition2, True)

        condition3 = user_story_23.uniqueNameAndBirth(GedcomClass.get_individual('I7', individuals), individuals)
        self.assertEqual(condition3, False)

        file.close()

    def test_us24(self):
        file = open('./Sprint3/test_ged/user_story_24_test.ged', 'r')
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
        file = open('./Sprint3/test_ged/user_story_28_test.ged', 'r')
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
        file = open('./Sprint3/test_ged/user_story_18_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)

        condition1 = user_story_18.siblings_not_married(GedcomClass.get_family('F1', families), individuals)
        self.assertEqual(condition1, True)

        condition2 = user_story_18.siblings_not_married(GedcomClass.get_family('F2', families), individuals)
        self.assertEqual(condition2, False)

        file.close()

class TestMethods4(unittest.TestCase):
    def test_us42(self):
        file = open('./Sprint4/test_ged/user_story_42_test.ged', 'r')
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
        file = open('./Sprint4/test_ged/user_story_34_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)

        condition1 = user_story_34.list_large_age_differences(individuals, families)
        self.assertEqual(condition1, ['F1'])

        file.close()


    def test_us31(self):
        file = open('./Sprint4/test_ged/user_story_31_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        condition1 = US_31.living_singles(individuals)
        self.assertListEqual(condition1, ['I3', 'I4'])
        file.close()

    def test_us38(self):
        file = open('./Sprint4/test_ged/user_story_38_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        condition1 = US_38.upcoming_births(individuals)
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
        condition1 = user_story_33.recentOrphans(families, individuals)
        self.assertEqual(condition1, ['I3'])

    def test_us39(self):
        file = open('./test_ged/user_story_33_test.ged', 'r')
        individuals = GedcomClass.read_individuals(file)
        families = GedcomClass.read_families(file)
        condition1 = user_story_39.upcomingAnniversaries(families, individuals)
        self.assertEquals(condition1, ["21 Nov 1973"])

if __name__ == "__main__":
    unittest.main()

