# Marriage should occur before divorce of spouses, and divorce can only occur after marriage

# Marriage should occur before death of either spouse

import Gedcom
from datetime import datetime
import unittest

file = open('./Test GEDCOM Files/JULIE GEDCOM.ged', 'r')
individuals = Gedcom.read_individuals(file)
family = Gedcom.read_families(file)


def is_marriage_before_divorce(family_id, families):
    marriage = families.get(family_id).get('MARR')
    divorce = families.get(family_id).get('DIV')

    if len(marriage) == 0:
        return False
    marriage_date = datetime.strptime(marriage[0], '%d %b %Y')
    if len(divorce) == 0:
        divorce_date = datetime.today()
    else:
        divorce_date = datetime.strptime(divorce[0], '%d %b %Y')

    if divorce_date.year >= marriage_date.year:
        if divorce_date.month >= marriage_date.month:
            if divorce_date.day >= marriage_date.day:
                return True
    return False


def is_marriage_before_death(family_id, families, individuals):
    marriage = families.get(family_id).get('MARR')

    husband = individuals.get(families.get(family_id).get('HUSB')[0]).get('DEAT')
    wife = individuals.get(families.get(family_id).get('WIFE')[0]).get('DEAT')

    if len(marriage) == 0:
        return False
    marriage_date = datetime.strptime(marriage[0], '%d %b %Y')

    if len(husband) == 0:
        husband_date = datetime.today()
    else:
        husband_date = datetime.strptime(husband[0], '%d %b %Y')
    if len(wife) == 0:
        wife_date = datetime.today()
    else:
        wife_date = datetime.strptime(wife[0], '%d %b %Y')

    if husband_date.year >= marriage_date.year and wife_date.year >= marriage_date.year:
        if husband_date.month >= marriage_date.month and wife_date.month >= marriage_date.month:
            if husband_date.day >= marriage_date.day and wife_date.day >= marriage_date.day:
                return True
    return False


print(is_marriage_before_divorce('F3', family))
print(is_marriage_before_death('F3', family, individuals))