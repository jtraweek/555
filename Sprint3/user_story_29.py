'''
@author: Maryam
Created: 10/27/2017
'''
'''
   User Story 29: list deceased indivisuals
   :return: A list of all indivisuals who are dead
'''


def deceased_people(individuals):
    deceased = []
    # getting every individual id from individuals dictionary.
    for indi in individuals.values():
        # allocate the instance of each of those id's
        # now that we got the instance of individuals you can use their attribute to pull their info's
        if not indi.alive:
            deceased.append(indi.id)

    return deceased
