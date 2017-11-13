"""
File addresses all outputs for Sprint 4
"""
import GedcomClass
from Sprint4 import US_31
from Sprint4 import US_38
from Sprint4 import user_story_34
from Sprint4 import user_story_42

file = open('./test_ged/user_story_31_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
print('\nTest user story 31 No Living Singles:')
GedcomClass.main(file)
if len(US_31.living_singles(individuals)) == 0:
    print('Error: US31: No Living Singles')
else:
    print('INFORMATION: INDIVIDUAL: US31: The list of living singles is {}'
          .format(US_31.living_singles(individuals)))

file = open('./test_ged/user_story_38_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
print('\nTest user story 38:')
GedcomClass.main(file)
print('INFORMATION: INDIVIDUAL: US38: The list of upcoming birthdays is {}'
      .format(US_38.upcoming_births(individuals)))

file = open('./test_ged/user_story_34_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('\nTest user story 34:')
GedcomClass.main(file)
print('INFORMATION: FAMILY: US34: The list of large age difference couples is {}'
      .format(user_story_34.list_large_age_differences(individuals, families)))

file = open('./test_ged/user_story_42_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('\nTest user story 42:')
GedcomClass.main(file)
for individual in individuals.values():
    if not user_story_42.is_date_valid(individual):
        print('ERROR: INDIVIDUAL: US42: Invalid dates occurs in {}'
              .format(individual.id))
for family in families.values():
    if not user_story_42.is_date_valid(family):
        print('ERROR: FAMILY: US42: Invalid dates occurs in {}'
              .format(family.id))
