# Marriage should occur before divorce of spouses, and divorce can only occur after marriage

# Marriage should occur before death of either spouse

import Gedcom
from datetime import datetime
import unittest

file = open('./Test GEDCOM Files/Liu ged.ged', 'r')
individuals = Gedcom.read_individuals(file)
families = Gedcom.read_families(file)


def is_marriage_before_divorce(family_id, families):
    marriage = Gedcom.get_args(family_id, 'MARR', families)
    divorce = Gedcom.get_args(family_id, 'DIV', families)

    if marriage == 'NA':
        return False
    marriage_date = datetime.strptime(marriage, '%d %b %Y')
    if divorce == 'NA':
        divorce_date = datetime.today()
    else:
        divorce_date = datetime.strptime(divorce, '%d %b %Y')

    if divorce_date.year >= marriage_date.year:
        if divorce_date.month >= marriage_date.month:
            if divorce_date.day >= marriage_date.day:
                return True
    return False


def is_marriage_before_death(family_id, families, individuals):
    marriage = Gedcom.get_args(family_id, 'MARR', families)

    husband = Gedcom.get_args(Gedcom.get_args(family_id, 'HUSB', families), 'DEAT', individuals)
    wife = Gedcom.get_args(Gedcom.get_args(family_id, 'WIFE', families), 'DEAT', individuals)

    if marriage == 'NA':
        return False
    marriage_date = datetime.strptime(marriage, '%d %b %Y')

    if husband == 'NA':
        husband_date = datetime.today()
    else:
        husband_date = datetime.strptime(husband, '%d %b %Y')
    if wife == 'NA':
        wife_date = datetime.today()
    else:
        wife_date = datetime.strptime(wife, '%d %b %Y')

    if husband_date.year >= marriage_date.year and wife_date.year >= marriage_date.year:
        if husband_date.month >= marriage_date.month and wife_date.month >= marriage_date.month:
            if husband_date.day >= marriage_date.day and wife_date.day >= marriage_date.day:
                return True
    return False


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
        self.assertTrue(Gedcom.dates_before_current_indi('18 DEC 0230', '9 MAY 0280'))
        
    def test_I7_dates_before_now(self):
        self.assertTrue(Gedcom.dates_before_current_indi('11 OCT 0283', 'NA'))    
        
    def test_invalid_birth_before_now(self):
        self.assertFalse(Gedcom.dates_before_current_indi('11 OCT 2020', 'NA'))

    def test_invalid_death_before_now(self):
        self.assertFalse(Gedcom.dates_before_current_indi('11 FEB 2016', '10 MAR 2021'))
        
    def test_invalid_marriage_before_now(self):
        self.assertFalse(Gedcom.dates_before_current_fam('11 OCT 2018', 'NA'))  
    
    def test_invalid_divorce_before_now(self):
        self.assertFalse(Gedcom.dates_before_current_fam('11 DEC 2016', '14 JAN 2018'))        

if __name__ == '__main__':
    unittest.main()
    