import GedcomClass
from Sprint3 import user_story_23
from Sprint3 import user_story_24

file = open('./test_ged/user_story_23_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
GedcomClass.main(file)
for individual in individuals.values():
    if not user_story_23.uniqueNameAndBirth(individual, individuals):
        print('Error: INDIVIDUAL: US23: {}: Name and Birthday are not unique for the individual'
              .format(individual.id))

file = open('./test_ged/user_story_24_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for family in families.values():
    if not user_story_24.uniqueSpousesAndMarriage(family, families, individuals):
        print('Error: FAMILY: US24: {}: Spouse information and Marriage dates are not unique for this family'
              .format(individual.id))