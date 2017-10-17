# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:20:23 2017
@author: Julie
User Story 11: No bigamy
An individual should only have one spouse at a time
"""
import Gedcom
from datetime import datetime


def no_bigamy(person):
    spouses = individuals[person]['FAMS']
    
    if len(spouses) < 2:
        return True
        
    marriage_date_ranges = []
        
    for item in spouses:
        fam_id = item.replace('@', '')
        marriage_date = Gedcom.get_args(fam_id, 'MARR', families)
        divorce_date = Gedcom.get_args(fam_id, 'DIV', families)
        
        if person == Gedcom.get_args(fam_id, 'WIFE', families):
            spouse_id = Gedcom.get_args(fam_id,'HUSB', families)
        else:
            spouse_id = Gedcom.get_args(fam_id, 'WIFE', families)
        spouse_death_date = Gedcom.get_args(spouse_id, 'DEAT', individuals)
        
        if divorce_date == 'NA' and spouse_death_date == 'NA':
            return False
        else:
            marriage_start_date = datetime.strptime(marriage_date, '%d %b %Y') 
            
        if divorce_date != 'NA':
            marriage_end_date = datetime.strptime(divorce_date, '%d %b %Y')
        else:
            marriage_end_date = datetime.strptime(spouse_death_date, '%d %b %Y')
        
        marriage_date_ranges.append((marriage_start_date, marriage_end_date))
    
    index = 0
    count = 1
    
    while count < len(marriage_date_ranges):
        marriage_start_1, marriage_end_1 = marriage_date_ranges[index]
        marriage_start_2, marriage_end_2 = marriage_date_ranges[index + 1]
        if marriage_start_1.date() <= marriage_end_2.date() and marriage_end_1.date() >= marriage_start_2.date():
            return False
        count += 1
        index += 1
    return True
                                


