'''
@author: Maryam
Created: 10/27/2017
'''
'''
   User Story 29: list living married indivisuals
   :return: A list of all indivisuals who are living and married
'''
import GedcomClass


def living_married(families, individuals):
    lm = []
    # fetching every family number from the spouse list in Individual class
    for fam in families.values():
        if fam.div_str == 'NA':
            # getting every individual id from individuals dictionary.
            # allocate the instance of each of those id's
            # now that we got the instance of individuals you can use their attribute to pull their info's
            husb = GedcomClass.get_individual(fam.husb, individuals)
            wife = GedcomClass.get_individual(fam.wife, individuals)
            if husb.alive:
                lm.append(husb.id)
            if wife.alive:
                lm.append(wife.id)
    return lm
