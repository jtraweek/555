# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 01:58:09 2017
@author: Julie
User story 18: Checks to ensure siblings are not married
"""
import GedcomClass

def siblings_not_married(family, individuals):
    husb = GedcomClass.get_individual(family.husb, individuals)
    wife = GedcomClass.get_individual(family.wife, individuals)
    husb_fam = husb.child_of
    wife_fam = wife.child_of
    if husb_fam == wife_fam:
        return False
    return True