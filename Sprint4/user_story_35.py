"""
Created on Tue Nov 14 14:50:41 2017
@author: Julie
User story 35: List all people in a Gedcom file who were born in the last 30 days
"""
from datetime import datetime, timedelta

def recently_born(individuals):
    recently_born = []
    for indi in individuals.values():
        birth = indi.birt
        time_dif = datetime.now() - birth
        if time_dif.days < 30:
            recently_born.append(indi.id)
    return recently_born