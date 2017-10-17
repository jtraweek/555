# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:21:29 2017
@author: Julie
User Story 10: Marriage after 14
Marriage dates should only occur after the individual has turned 14 years of age.
"""
from dateutil import relativedelta


def marriage_after_14(birthday, marriage):
    if marriage == 'NA':
        return 'Not married'
    else:
        age_at_marriage = relativedelta.relativedelta(marriage, birthday)
        if 0 <= age_at_marriage.years < 14:
            return False
        else:
            return True
