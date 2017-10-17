#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 11:12:36 2017

@author: celestesakhile
class for creating Family
"""

from datetime import datetime


class Family(object):
    def __init__(self):
        """
        Init all the attributes except list ones with None
        Init list attributes with blank list
        """
        self._id = None
        self._id_count = 1
        self._wife = None
<<<<<<< HEAD
        self._wifeName = None
        self._div = None
        self._marr = None
        self._husb = None
        self._husbName = None
=======
        self._husb = None
        self._marr = None
        self._div = None
>>>>>>> d893aa66d5067761192c3d2e149c62c49c297a76
        self._chil = []

    @property
    def id(self):
        """
        Getter
        :return 'NA' on missing records
        """
        if not self._id:
            return 'NA'
        return self._id

    @id.setter
    def id(self, _id):
        """
        Setter
        Replace the attribute with given object
        """
        self._id = _id

    @property
    def wife(self):
        if not self._wife:
            return 'NA'
        return self._wife

    @wife.setter
    def wife(self, wife):
        self._wife = wife

    @property
    def wifeName(self):
        if not self._wifeName:
            return 'NA'
        return self._wifeName

    @wifeName.setter
    def wifeName(self, wifeName):
        self._wifeName = wifeName
        
    @property
    def div(self):
        if not self._div:
            return 'NA'
        return self._div

    @div.setter
    def div(self, div):
        self._div = datetime.strptime(div, '%d %b %Y')

    @property
    def div_str(self):
        if not self._div:
            return 'NA'
        return self._div.strftime('%d %b %Y')

    @property
    def marr(self):
        if not self._marr:
            return 'NA'
        return self._marr

    @marr.setter
    def marr(self, marr):
        self._marr = datetime.strptime(marr, '%d %b %Y')

    @property
    def marr_str(self):
        if not self._marr:
            return 'NA'
        return self._marr.strftime('%d %b %Y')

    @property
    def husb(self):
        if not self._husb:
            return 'NA'
        return self._husb

    @husb.setter
    def husb(self, husb):
        self._husb = husb

    @property
    def husbName(self):
        if not self._husbName:
            return 'NA'
        return self._husbName

    @husbName.setter
    def husbName(self, husbName):
        self._husbName = husbName
        
    @property
    def chil(self):
        """
        Default getter for list attributes
        :return the list object
        """
        if not self._chil:
            return 'NA'
        return self._chil

    @chil.setter
    def chil(self, chil):
        """
        Setter for list attributes
        Append the given object to the list
        """
        self._chil.append(chil)

    @chil.deleter
    def chil(self):
        """
        Deleter for list attributes
        """
        self._chil = []

    @property
    def chil_str(self):
        """
        String getter for list attributes
        :return the string version of the list object
                append commas for multiple values
        """
        if not self._chil:
            return 'NA'
        string = ''
        for c in self._chil:
            string += c + ', '
        string = string[:-2]
        return string

    @property
    def id_count(self):
        return self._id_count

    @id_count.setter
    def id_count(self, count):
        self._id_count = count
