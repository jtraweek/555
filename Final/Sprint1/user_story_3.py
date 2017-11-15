'''
@author: Maryam
Created: 10/17/2017
'''

from datetime import datetime
import GedcomClass

'''
   User Story 3: Birth before Death
   Birth date should occur before death date for an indivisual 
   :return: True on valid dates after comparing both dates
'''

'''
Creating the instance should be derived from the GedcomClass. 
The GedcomClass returns a dictionary of indivisuals 

'''


def bir_deth(person):
    # this method will compare between birth and date to find legit date format.
    birth = person.birt
    death = person.deat

    if birth == 'NA' or death == 'NA':
        return True

    if birth <= death:
        return True
    return False
