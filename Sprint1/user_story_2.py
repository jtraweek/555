'''
@author: Maryam
Created: 10/17/2017
'''
from datetime import datetime
import GedcomClass
import Gedcom
"""
   User Story 2: Birth before Marriage
   Birth date should occur before Marriage date for an indivisual 
   :return: True on valid dates after comparing both dates
"""

file = open('./Test GEDCOM Files/JULIE GEDCOM.ged', 'r')
indivisuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
person = indivisuals.get()
family = families.get()

def bir_marriage(family,person):
    # this method will ensure that the birth date is before the marriage date.
    Birth = person.birt_str
    Marriage = family.marr_str

    if Birth == 'NA' or Marriage == 'NA':
        return True

    if Birth >= Marriage:
        return True
    return False