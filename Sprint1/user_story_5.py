# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:17:08 2017
"""
from datetime import datetime
import Gedcom

def is_marriage_before_death(person_id, family_id, families, individuals):
    """
    User Story 5: Marriage before death
    Marriage should occur before death of either spouse
    :return: True on valid marriage date
    """
    marriage = Gedcom.get_args(family_id, 'MARR', families)

    # get death record of family
    deat = Gedcom.get_args(person_id, 'DEAT', individuals)

    if marriage == 'NA':
        return True
    marriage_date = datetime.strptime(marriage, '%d %b %Y')

    # if no death record found
    # set it today
    if deat == 'NA':
        date = datetime.today()
    else:
        date = datetime.strptime(deat, '%d %b %Y')

    if date >= marriage_date:
        return True
    return False