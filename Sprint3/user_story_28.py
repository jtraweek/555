# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 00:12:08 2017

@author: Julie

User story 28: Sorts list of siblings by age from oldest to youngest. 
"""
import GedcomClass

def order_siblings_by_age(family, individuals):
    children = family.chil
    sibling_ages = list()
    siblings_ordered = list()
    
    if children == 'NA':
        return 'No children'
        
    if len(children) == 1:
        return 'Only one child'
    
    for child in children:
        current_child = GedcomClass.get_individual(child, individuals)
        child_age = current_child.age
        sibling_ages.append(tuple((child, child_age)))
    
    siblings_sorted = sorted(sibling_ages, key=lambda x: x[1], reverse = True)
    
    for item in siblings_sorted:
        siblings_ordered.append(item[0])
    
    return siblings_ordered
        
    
    
    