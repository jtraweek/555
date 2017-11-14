# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 15:39:59 2017
@author: Julie
User story 36: List all people in a Gedcom file who died in the last 30 days
"""
from datetime import datetime

def recently_dead(individuals):
    recently_dead = []
    for indi in individuals.values():
        death = indi.deat
        time_dif = datetime.now() - death
        if time_dif.days < 30:
            recently_dead.append(indi.id)
    return recently_dead