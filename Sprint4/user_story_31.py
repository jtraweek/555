'''
@author: Maryam
Created: 11/9/2017
'''
'''
   User Story 29: list living single indivisuals
   :return: A list of all indivisuals who are living, un-married, and over 30
'''


def living_singles(individuals):
    ls = []
    # fetching every family number from the spouse list in Individual class

    for individual in individuals.values():
        if individual.spouse_of== 'NA' and individual.alive and individual.age > 30:
            # getting every individual id from individuals dictionary.
            # allocate the instance of each of those id's
            # now that we got the instance of individuals you can use their attribute to pull their info's
            ls.append(individual.id)

    return ls
