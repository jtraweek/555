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


def get_age(person_id, individuals):
    """
    This function checks for the age of an individual.
    It either returns the age or 'NA'
    """

    def age(self):
        """
        Built-in age calculation
        :return: 'NA' on older than 150 or younger than 0
        """
        Birthday = person_istance.birt
        Deathday = person_istance.deat
        if not Birthday:
            return 'NA'

        birth = Birthday
        if not Deathday:
            death = datetime.today()
        else:
            death = Deathday
        age = death.year - birth.year
        if age < 150:
            return age
        return 'NA'
