# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:17:08 2017
"""


def is_marriage_before_death(person, family):
    """
    User Story 5: Marriage before death
    Marriage should occur before death of either spouse
    :return: True on valid marriage date
    """
    marriage = family.marr

    # get death record of family
    deat = person.deat

    if marriage == 'NA' or deat == 'NA':
        return True

    if deat > marriage:
        return True
    return False
