
'''
@author: Maryam
Created: 10/17/2017
'''

import Individual
import GedcomClass

"""
   User Story 8: Birth before Marriage
   Birth of spouse and their marriage date should occur before Marriage date for an indivisual
   :return: True on valid dates after checking the spouse marriage and birth dates and then the indivisual.
"""
file = open('./Test GEDCOM Files/JULIE GEDCOM.ged', 'r')
indivisuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
ind = indivisuals.get()
fam = families.get()

def birth_before_marriage(ind,fam):
    """
    This function checks if a child is born before the marriage of their parents
    """
    for family_id in fam:
        marriage = fam.marr_str
        children_list = fam.chil_str

        if len(children_list) != 0:

            for child in children_list:
                if child == ind.id:
                    birth = ind.child.birt
                    diff_birth_marr = int(birth) - int(marriage)
                    if diff_birth_marr < 0:
                        return False
                    else:
                        return True

    return False
