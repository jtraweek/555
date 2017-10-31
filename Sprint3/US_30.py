'''
@author: Maryam
Created: 10/27/2017
'''
'''
   User Story 29: list deceased indivisuals
   :return: A list of all indivisuals who are dead
'''
import GedcomClass
from Individual import Individual


def deceased_people(indivisual,individuals):
    deceased = []
    # getting every indivisual id from indivisuals dictionary.
    for id in individuals:
        #allocate the instane of each of those id's
        indi = GedcomClass.get_individual(id, individuals)
        #now that we got the instance of indivisuals you can use their attribute to pull their info's
        if indi.alive()!= True:
            deceased_indi = indi.deat_str
            deceased.append(deceased_indi)
            
    return deceased
