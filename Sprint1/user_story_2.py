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
'''
file = open('./Test GEDCOM Files/JULIE GEDCOM.ged', 'r')
indivisuals = GedcomClass.read_individuals(file)
ind-fam = indivisuals.spouse_str
'''

def bir_marriage(person_id, family_id, individuals, families):
    # this method will ensure that the birth date is before the marriage date.
    b = Gedcom.get_args(person_id, 'BIRT', individuals)
    m = Gedcom.get_args(family_id, 'MARR', families)

    if b == 'NA' or m == 'NA':
        return True
    b_date = datetime.strptime(b, '%d %b %Y')
    m_date = datetime.strptime(m, '%d %b %Y')

    if m_date >= b_date:
        return True
    return False