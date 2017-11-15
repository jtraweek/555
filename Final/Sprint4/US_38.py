'''
@author: Maryam
Created: 11/11/2017
'''
'''
   User Story 38: list upcoming birthdays
   :return: A list of all indivisuals who their birthdays coming within the 30 days. 
'''
import GedcomClass
from datetime import datetime, timedelta


def upcoming_births(individuals):
    births = []
    # fetching every indivisual from the Individual class
    # getting every individual birth from individuals dictionary.
    today = datetime.today()
    upcoming30 = today + timedelta(days=30)
    for indi in individuals.values():
        if indi.birt_str != 'NA':
            if today <= indi.birt <= upcoming30:
                births.append(indi.id)
    return births
