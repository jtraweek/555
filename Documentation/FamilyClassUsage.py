#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:41:08 2017

@author: celestesakhile
"""

# import the class
from Family import Family

# create a new instance
fam = Family()

# calling attributes before setting values
print('First test:')
print(fam.id)
print(fam.wife)
print(fam.wifeName)
print(fam.div)
print(fam.div_str)
print(fam.marr)
print(fam.marr_str)
print(fam.husb)
print(fam.husbName)
print(fam.chil)
print(fam.chil_str)

# set values
# the normal setter will replace the built-in attributes with the given object
print('Second test:')
fam.id = 'F01'
fam.wife = 'I02'
fam.wifeName = 'Stella'
fam.husb = 'I01'
fam.husbName = 'Ted'
fam.marr = '13 OCT 2000'
fam.div = '16 DEC 2016'
fam.chil = 'BABY'
print(fam.id)
print(fam.wife)
print(fam.wifeName)
print(fam.div)
print(fam.div_str)
print(fam.marr)
print(fam.marr_str)
print(fam.husb)
print(fam.husbName)
print(fam.chil)
print(fam.chil_str)
# note that the date attribute has two getters
# default getter will return a datetime object
# _str getter will return a format date string

# IMPORTANT
# note that the list attributes have different implementation of setter
# list setter will only append the given object to the list attributes
print('Third test:')
fam.chil = 'BABY1'
# the list attributes also have two getters
# normal getter will return list object
# _str getter will return a string version of the list
print(fam.chil)
print(fam.chil_str)
fam.chil = 'BABY2'
print(fam.chil)
print(fam.chil_str)

# list attributes have a deleter
print('Fourth test:')
del fam.chil
print(fam.chil)
print(fam.chil_str)
