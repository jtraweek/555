
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


def birth_before_marriage(family, individual_id, individuals):
    """
    This function checks if a child is born before the marriage of their parents
    """
    for family_id in family:
        marr = family.get(family_id).get('MARR')[0].split(' ')[-1]
        children_list = family.get(family_id).get('CHIL')

        if len(children_list) != 0:

            for child in children_list:
                if child == individual_id:
                    birth = individuals.get(child).get('BIRT')[0].split(' ')[-1]
                    diff_birth_marr = int(birth) - int(marr)
                    if diff_birth_marr < 0:
                        return False
                    else:
                        return True

    return False
