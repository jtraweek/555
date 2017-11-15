#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 19:46:07 2017

@author: celestesakhile
"""

from dateutil.relativedelta import relativedelta

"""
   User Story 9: Birth before death of parents
   Child should be born before death of mother and before 9 months after death of father
   :return: True on valid dates after checking the parent marriage and death dates and then the individual.
"""


def birth_before_parents_death(person_id, individuals, families):
    person = individuals.get(person_id)
    family_id = person.child_of
    child_birth = person.birt
    if family_id == 'NA' or child_birth == 'NA':
        return True

    family = families.get(family_id)
    husb = individuals.get(family.husb)
    wife = individuals.get(family.wife)

    if not husb.alive:
        husb_deat = husb.deat + relativedelta(months=9)
        if child_birth > husb_deat:
            return False
    if not wife.alive:
        wife_deat = wife.deat
        if child_birth > wife_deat:
            return False
    return True
