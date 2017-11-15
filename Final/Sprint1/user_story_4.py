# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:08:04 2017
"""


def is_marriage_before_divorce(family):
    """
    User Story 4: Marriage before divorce
    Marriage should occur before divorce of spouses, and divorce can only occur after marriage
    :return: True on valid marriage date
    """
    marriage = family.marr
    divorce = family.div

    if marriage == 'NA' or divorce == 'NA':
        return True

    if divorce >= marriage:
        return True
    return False
