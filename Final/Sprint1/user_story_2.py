"""
@author: Maryam
Created: 10/17/2017
"""

"""
   User Story 2: Birth before Marriage
   Birth date should occur before Marriage date for an indivisual 
   :return: True on valid dates after comparing both dates
"""


def bir_marriage(person, family):
    # this method will ensure that the birth date is before the marriage date.
    birth = person.birt
    marriage = family.marr

    if birth == 'NA' or marriage == 'NA':
        return True

    if birth <= marriage:
        return True
    return False
