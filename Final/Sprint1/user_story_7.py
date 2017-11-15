'''
@author: Maryam
Created: 10/17/2017
'''

import GedcomClass
from datetime import datetime

"""
   User Story 7: Legit age for indivisual
   Assuring an indivisual has a date bigger than 0 and less than 150
   :return: True on valid
"""


def age_not_too_old(person):
    return person.age != 'NA'
