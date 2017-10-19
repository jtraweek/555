# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:42:27 2017

@author: Julie
"""


def div_b4_death(person, family):
    """
    Ensures divorce date occurred after death of husband & wife
    """
    divorce = family.div
    death = person.deat

    if divorce == 'NA':
        return 'No divorce'
    elif death == 'NA':
        return 'No death'
    else:
        if divorce > death:
            return False
        else:
            return True
