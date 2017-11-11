'''
@author: Maryam
Created: 11/9/2017
'''
'''
   User Story 29: list living single indivisuals
   :return: A list of all indivisuals who are living, un-married, and over 30
'''
import GedcomClass


def living_singles(families, individuals):
    ls = []
    # fetching every family number from the spouse list in Individual class
    for fam in families.values():
        if fam.marr_str == 'NA':
            # getting every individual id from individuals dictionary.
            # allocate the instance of each of those id's
            # now that we got the instance of individuals you can use their attribute to pull their info's
            husb = GedcomClass.get_individual(fam.husb, individuals)
            wife = GedcomClass.get_individual(fam.wife, individuals)
            if husb.alive and husb.age > 30:
                ls.append(husb.id)
            if wife.alive and wife.age > 30:
                ls.append(wife.id)
    return ls
