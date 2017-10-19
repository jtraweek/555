'''
@author: Maryam
Created: 10/17/2017
'''

from dateutil.relativedelta import relativedelta

"""
   User Story 8: Birth before Marriage
   Birth of spouse and their marriage date should occur before Marriage date for an indivisual
   :return: True on valid dates after checking the spouse marriage and birth dates and then the indivisual.
"""


def birth_before_marriage(person, family):
    """
    This function checks if a child is born before the marriage of their parents
    """
    marr = family.marr
    birt = person.birt
    div = family.div
    if birt == 'NA' or (marr == 'NA' and div == 'NA'):
        return True

    if marr > birt:
        return False

    if div != 'NA':
        div_nine_after = div + relativedelta(months=9)
        if birt > div_nine_after:
            return False
    return True
