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

def parents_not_too_old(family_id, individual_id, individuals, families):
    
    family = families.get(family_id)
    husb_id = family.husb
    wife_id = family.wife
    
    husb_info = individuals.get(husb_id)
    wife_info = individuals.get(wife_id)
    
    husb_age= husb_info.age
    wife_age= wife_info.age
    
    
    if family.chil == 'NA':
            return False
    
    for child_id in family.chil:
        child = individuals.get(child_id)
        if child == individual_id:
            child_age = child.age
            if (wife_age - child_age < 60 ) and (husb_age - child_age < 80 ) :
                return True
            else:
                return False
            
