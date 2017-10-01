import Gedcom
import unittest

class TestMethods(unittest.TestCase):
    def test_f1_divorce(self):
        self.assertTrue(is_marriage_before_divorce('F1', families))

    def test_f1_death(self):
        self.assertFalse(is_marriage_before_death('F1', families, individuals))

    def test_f2_divorce(self):
        self.assertFalse(is_marriage_before_divorce('F2', families))

    def test_f2_death(self):
        self.assertTrue(is_marriage_before_death('F2', families, individuals))

    def test_f3_divorce(self):
        self.assertTrue(is_marriage_before_divorce('F3', families))

    def test_f3_death(self):
        self.assertTrue(is_marriage_before_death('F3', families, individuals))
        
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
        

if __name__ == '__main__':
    unittest.main()
    