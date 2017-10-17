# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:08:04 2017
"""
import Gedcom
from datetime import datetime

def is_marriage_before_divorce(family_id, families):
    """
    User Story 4: Marriage before divorce
    Marriage should occur before divorce of spouses, and divorce can only occur after marriage
    :return: True on valid marriage date
    """
    marriage = Gedcom.get_args(family_id, 'MARR', families)
    divorce = Gedcom.get_args(family_id, 'DIV', families)

    if marriage == 'NA':
        return True
    marriage_date = datetime.strptime(marriage, '%d %b %Y')

    # if no divorce record found
    # set it today
    if divorce == 'NA':
        divorce_date = datetime.today()
    else:
        divorce_date = datetime.strptime(divorce, '%d %b %Y')

    if divorce_date >= marriage_date:
        return True
    return False