# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:21:29 2017
@author: Julie
User Story 10: Marriage after 14
Marriage dates should only occur after the individual has turned 14 years of age.
"""
from datetime import datetime
from dateutil import relativedelta 

def marriage_after_14(birthday, marriage):
    if marriage == 'NA':
        return 'Not married'
    else:
        marriage_date = datetime.strptime(marriage, '%d %b %Y')
        age_at_marriage = relativedelta.relativedelta(marriage_date, birthday)
        print(age_at_marriage.years)
        if age_at_marriage.years <= 14:
            return False
        else:
            return True 

        
