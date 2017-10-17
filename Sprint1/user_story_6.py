# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:42:27 2017

@author: Julie
"""

def div_b4_death(divorce, death):
    """
    Ensures divorce date occurred after death of husband & wife
    """
    if divorce == 'NA':
        return 'No divorce'
    elif death == 'NA':
        return 'No death'
    else:
        if divorce.date() > death.date():
            return False
        else:
            return True