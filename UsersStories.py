import Gedcom
import unittest
import datetime

def bir_deth(b,d):
    # this method will compare between birth and date to find legit date format.

    for item in indivisuals:
        b = Gedcom.get_args(item, 'BIRT', indivisuals)
        d = Gedcom.get_args(item, 'DEAT', indivisuals)
        indi_birth_date = datetime.datetime.strptime(b, '%d %b %Y')
        indi_death_date = datetime.datetime.strptime(d, '%d %b %Y')
        if b or d !='NA'and indi_birth_date > indi_death_date:
            return True
        return False



def main(file):
    individuals = read_individuals(file)
    family = read_families(file)
    file = open('C:\\Users/Maryam/Documents/GitHub/555/Test GEDCOM Files/JULIE GEDCOM.ged', 'r')
    main(file)
