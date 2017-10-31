'''
@author: Maryam
Created: 10/27/2017
'''
'''
   User Story 29: list living married indivisuals
   :return: A list of all indivisuals who are living and married
'''
import GedcomClass
from Family import Family
from Individual import Individual


def living_married(indivisual,families,individuals):
    lm = []
    # getting every indivisual id from indivisuals dictionary.
    for id in individuals:
        #allocate the instane of each of those id's
        indi = GedcomClass.get_individual(id, individuals)
        #now that we got the instance of indivisuals you can use their attribute to pull their info's
        living = indi.alive()
        #fgeting every family number from the spouse list in Indivisual class
        for famid in indi.spouse_str:
            fam = GedcomClass.get_family(famid,families)
            if not fam.div_str:
                married = fam.marr_str
                lm.append(married)
    return lm




