"""
File addresses all outputs for Sprint 3
"""
import GedcomClass
from Sprint3 import user_story_13
from Sprint3 import user_story_18
from Sprint3 import user_story_21
from Sprint3 import user_story_23
from Sprint3 import user_story_24
from Sprint3 import user_story_28
from Sprint3 import US_29
from Sprint3 import US_30

file = open('./test_ged/user_story_13_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('Test user story 13:')
GedcomClass.main(file)
for individual in individuals.values():
    family = GedcomClass.get_family(individual.child_of, families)
    if not user_story_13.siblings_spacing(individual, family, individuals):
        print('Error: FAMILY: US13: {}: Birth dates of siblings are more than 2 days and less than 8 months'
              .format(family.id))

file = open('./test_ged/user_story_18_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('\n Test user story 18:')
GedcomClass.main(file)
for family in families.values():
    if not user_story_18.siblings_not_married(family, individuals):
         print('Error: FAMILY: US18: {}: Siblings are married.'
              .format(family.id))

file = open('./test_ged/user_story_21_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('\n Test user story 21:')
GedcomClass.main(file)
for family in families.values():
    if not user_story_21.correct_gender(family, individuals):
        print('Error: FAMILY: US21: {}: Husband is not male or wife is not female'
              .format(family.id))

file = open('./test_ged/user_story_23_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
print('\n Test user story 23:')
GedcomClass.main(file)
for individual in individuals.values():
    if not user_story_23.uniqueNameAndBirth(individual, individuals):
        print('Error: INDIVIDUAL: US23: {}: Name and Birthday are not unique for the individual'
              .format(individual.id))

file = open('./test_ged/user_story_24_test.ged', 'r')
families = GedcomClass.read_families(file)
individuals = GedcomClass.read_individuals(file)
print('\n Test user story 13:')
GedcomClass.main(file)
for family in families.values():
    if not user_story_24.uniqueSpousesAndMarriage(family, families, individuals):
        print('Error: FAMILY: US24: {}: Spouse information and Marriage dates are not unique for this family'
              .format(family.id))

file = open('./test_ged/user_story_28_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('\n Test user story 28:')
GedcomClass.main(file)
for family in families.values():
    if user_story_28.order_siblings_by_age(family, individuals)=='No children':
        print('Error: FAMILY: US28: {}: No children.'
              .format(family.id))
    elif user_story_28.order_siblings_by_age(family, individuals)=='Only one child':
         print('Error: FAMILY: US28: {}: Only one child.'
              .format(family.id))
    else:
        print('FAMILY: US28: {} ordered oldest to youngest.'.format(user_story_28.order_siblings_by_age(family, individuals)))

file = open('./test_ged/user_story_29_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
print('\n Test user story 29:')
GedcomClass.main(file)
if len(US_29.deceased_people(individuals)) == 0:
    print('Error: US29: No deceased')
else:
    print('INDIVIDUAL: US29: {}'.format(US_29.deceased_people(individuals)))

file = open('./test_ged/user_story_30_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('\n Test user story 30:')
GedcomClass.main(file)
print('INFORMATION: FAMILY: US30: The list of living married individuals is {}'
      .format(US_30.living_married(families, individuals)))
