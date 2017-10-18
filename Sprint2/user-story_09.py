#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 19:46:07 2017

@author: celestesakhile
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta


"""
   User Story 9: Birth before death of parents
   Child should be born before death of mother and before 9 months after death of father
   :return: True on valid dates after checking the parent marriage and death dates and then the individual.
"""

def birth_before_parents_death(family_id, individual_id, individuals, families):
    
    family = families.get(family_id)
    husb_id = family.husb
    wife_id = family.wife
    
    husb_info = individuals.get(husb_id)
    wife_info = individuals.get(wife_id)
    nine_mon_rel = relativedelta(months=9)
    
    if husb_info.alive == True and wife_info.alive == True:
        return False
        
    elif husb_info.alive == True and wife_info.alive == False:
        wife_deat = wife_info.deat
        if family.chil == 'NA':
            return False
        for child_id in family.chil:
            child = individuals.get(child_id)
            if child == individual_id:
                child_birth = child.birt
                if child_birth < wife_deat:
                    return False
                else:
                    return True
      
    elif husb_info.alive == False and wife_info.alive == True:
        husb_deat = husb_info.deat
        if family.chil == 'NA':
            return False
        for child_id in family.chil:
            child = individuals.get(child_id)
            if child == individual_id:
                child_birth = child.birt
                if child_birth < (nine_mon_rel + husb_deat):
                    return False
                else:
                    return True
        
    else: 
        husb_deat = husb_info.deat
        wife_deat = wife_info.deat
        if family.chil == 'NA':
            return False
        for child_id in family.chil:
            child = individuals.get(child_id)
            if child == individual_id:
                child_birth = child.birt
                if child_birth < (nine_mon_rel + husb_deat) and child_birth < wife_deat:
                    return False
                else:
                    return True
    