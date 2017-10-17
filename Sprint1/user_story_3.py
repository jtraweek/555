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
file = open('./Test GEDCOM Files/JULIE GEDCOM.ged', 'r')
indivisuals = GedcomClass.read_individuals(file)
person_istance = indivisuals.get()

def bir_deth(person_istance):
    # this method will compare between birth and date to find legit date format.
    birth = person_istance.birt_str
    death = person_istance.deat_str

    if birth == 'NA':
        return False

    if birth >= death:
        return True
    return False
