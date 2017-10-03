import Gedcom
import unittest
import UsersStories

class TestMethods(unittest.TestCase):
    def test_f1_divorce(self):
        self.assertTrue(Gedcom.is_marriage_before_divorce('F1', families))

    def test_f1_death(self):
        self.assertFalse(Gedcom.is_marriage_before_death('F1', families, individuals))

    def test_f2_divorce(self):
        self.assertFalse(Gedcom.is_marriage_before_divorce('F2', families))

    def test_f2_death(self):
        self.assertTrue(Gedcom.is_marriage_before_death('F2', families, individuals))

    def test_f3_divorce(self):
        self.assertTrue(Gedcom.is_marriage_before_divorce('F3', families))

    def test_f3_death(self):
        self.assertTrue(Gedcom.is_marriage_before_death('F3', families, individuals))
        
    def test_I1_dates_before_now(self):
        self.assertTrue(Gedcom.dates_b4_current_indi('18 DEC 0230', '9 MAY 0280'))
        
    def test_I7_dates_before_now(self):
        self.assertTrue(Gedcom.dates_b4_current_indi('11 OCT 0283', 'NA'))    
        
    def test_invalid_birth_before_now(self):
        self.assertFalse(Gedcom.dates_b4_current_indi('11 OCT 2020', 'NA'))

    def test_invalid_death_before_now(self):
        self.assertFalse(Gedcom.dates_b4_current_indi('11 FEB 2016', '10 MAR 2021'))
        
    def test_invalid_marriage_before_now(self):
        self.assertFalse(Gedcom.dates_b4_current_fam('11 OCT 2018', 'NA'))  
    
    def test_invalid_divorce_before_now(self):
        self.assertFalse(Gedcom.dates_b4_current_fam('11 DEC 2016', '14 JAN 2018'))  
    
    def test_no_death_div_b4_death(self):   
        self.assertTrue(Gedcom.div_b4_death('12 NOV 2014', 'NA', 'NA'))
    
    def test_valid_div_b4_death(self):
        self.assertTrue(Gedcom.div_b4_death('12 NOV 2014', '15 JAN 2015', '21 FEB 2017'))
    
    def test_div_after_wife_death_div_b4_death(self):
        self.assertFalse(Gedcom.div_b4_death('12 NOV 2014', '15 JAN 2015', '21 FEB 2013'))
        
    def test_div_after_husb_death_div_b4_death(self):
        self.assertFalse(Gedcom.div_b4_death('12 NOV 2014', '15 JAN 2012', '21 FEB 2017'))
        
    def test_div_after_both_death_div_b4_death(self):
        self.assertFalse(Gedcom.div_b4_death('12 NOV 2014', '15 JAN 2010', '21 FEB 2011'))
    
    def test_no_div_div_b4_death(self):
        self.assertTrue(Gedcom.div_b4_death('NA', '15 JAN 2015', '21 FEB 2017'))

    def test_birth_b4_death(self): # YOU ARE TESTING THE FUNCTION, NOT THE VALUES!
        self.assertFalse(UsersStories.bir_deth('NA','NA'))
        self.assertFalse(UsersStories.bir_deth(' ','NA'))
        self.assertFalse(UsersStories.bir_deth('31 MAY 2017 ','31 MAY 2017'))
        self.assertTrue(UsersStories.bir_deth('12 MAY 2013 ','NA'))
        self.assertGreater(UsersStories.bir_deth('24 JUNE 2010','28 MAR 1992'))

    def test_birth_b4_marriage(self):
        self.assertFalse(UsersStories.bir_marriage(' ',' '))
        self.assertFalse(UsersStories.bir_marriage('NA','NA'))
        self.assertTrue(UsersStories.bir_marriage('23 JAN 1988','24 APR 1992'))
        self.assertFalse(UsersStories.bir_marriage('23 JAN','24'))
        self.assertFalse(UsersStories.bir_marriage('23 JAN 14','24 JAN 1988'))
        self.assertFalse(UsersStories.bir_marriage('FOO','12 JAN 1234'))


if __name__ == '__main__':
    unittest.main()
    