# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:20:23 2017
@author: Julie
User Story 11: No bigamy
An individual should only have one spouse at a time
"""
from datetime import datetime


def no_bigamy(person, individuals, families):
    spouses = individuals.get(person).spouse
    if len(spouses) > 1:
        marriages = []
        divorces = []
        for item in spouses:
            family = families.get(item)
            marr = family.marr
            div = family.div
            if marr == 'NA':
                marr = datetime.today()
            if div == 'NA':
                div = datetime.today()

            marriages.append(marr)
            divorces.append(div)
        for m in range(0, len(marriages)):
            for d in range(0, len(divorces)):
                if marriages[d] < marriages[m] < divorces[d]:
                    return False
        for d in range(0, len(divorces)):
            for m in range(0, len(marriages)):
                if marriages[m] < divorces[d] < divorces[m]:
                    return False
    return True
