#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:23:67 2017

@author: celestesakhile
"""

"""
   User Story 12: Parents not too old
   Mother should be less than 60 years older than her children
   and father should be less than 80 years older than his children
   :return: True if conditions are satisfied
"""


def parents_not_too_old(person_id, individuals, families):
    person = individuals.get(person_id)
    family_id = person.child_of
    if family_id == 'NA':
        return True
    family = families.get(family_id)

    husb_birt = individuals.get(family.husb).birt
    wife_birt = individuals.get(family.wife).birt
    child_birt = person.birt

    if husb_birt == 'NA' or child_birt.year - husb_birt.year < 80:
        if wife_birt == 'NA' or child_birt.year - wife_birt.year < 60:
            return True
    return False
