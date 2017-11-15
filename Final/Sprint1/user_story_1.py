# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:42:27 2017

@author: Julie
"""

from datetime import datetime

def dates_b4_current_indi(date):
    """
    Checks birth, death dates to ensure they occurred before the current date
    """
    if date != 'NA':
        if date.date() < datetime.today().date():
            return True
        else:
            return False
    else:
        return 'No date available'