'''
@author: Maryam
Created: 11/11/2017
'''
'''
   User Story 41: list upcoming birthdays
   :return: A list of all indivisuals who their birthdays coming within the 30 days. 
'''
import GedcomClass
from datetime import datetime, timedelta


def upcoming_births(individuals):
    births = []
    # fetching every indivisual from the Individual class
    # getting every individual birth from individuals dictionary.
    Today = datetime.today()
    upcoming30 = Today + timedelta(days=30)
    for indi in individuals.values():
        if indi.birt_str != 'NA':
            if indi.birt_str <= upcoming30:
                births.append(indi.birt_str)
    return births
