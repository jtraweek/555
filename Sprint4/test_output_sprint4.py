"""
File addresses all outputs for Sprint 4
"""
import GedcomClass
from Sprint4 import US_31
from Sprint4 import US_38
from Sprint4 import user_story_34
from Sprint4 import user_story_42
from Sprint4 import user_story_35
from Sprint4 import user_story_36
from Sprint4 import user_story_33
from Sprint4 import user_story_39

file = open('./test_ged/user_story_31_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
print('\nTest user story 31: Living Singles:')
GedcomClass.main(file)
if len(US_31.living_singles(individuals)) == 0:
    print('Error: US31: No Living Singles')
else:
    print('INFORMATION: INDIVIDUAL: US31: The list of living singles is {}'
          .format(US_31.living_singles(individuals)))

file = open('./test_ged/user_story_34_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('\nTest user story 34: Large Age Difference: ')
GedcomClass.main(file)
print('INFORMATION: FAMILY: US34: The list of large age difference couples is {}'
      .format(user_story_34.list_large_age_differences(individuals, families)))


file = open('./test_ged/user_story_35+36_test_1.ged', 'r')
individuals = GedcomClass.read_individuals(file)
print('\nTest user story 35: Recent Born: ')
GedcomClass.main(file)
if len(user_story_35.recently_born(individuals)) == 0:
    print('Error: US35: No Recent Born')
else:
    print('INFORMATION: INDIVIDUAL: US35: The recent born indivisuals are {}'
          .format(user_story_35.recently_born(individuals)))


file = open('./test_ged/user_story_35+36_test_1.ged', 'r')
individuals = GedcomClass.read_individuals(file)
print('\nTest user story 36: Recent Death: ')
GedcomClass.main(file)
if len(user_story_36.recently_dead(individuals)) == 0:
    print('Error: US31: No Recent Deaths')
else:
    print('INFORMATION: INDIVIDUAL: US36: The recent dead indivisuals are {}'
          .format(user_story_36.recently_dead(individuals)))



file = open('./test_ged/user_story_38_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
print('\nTest user story 38: Upcoming Birthdays: ')
GedcomClass.main(file)
print('INFORMATION: INDIVIDUAL: US38: The list of upcoming birthdays is {}'
      .format(US_38.upcoming_births(individuals)))



file = open('./test_ged/user_story_42_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('\nTest user story 42: Validating Dates: ')
GedcomClass.main(file)
for individual in individuals.values():
    if not user_story_42.is_date_valid(individual):
        print('ERROR: INDIVIDUAL: US42: Invalid dates occurs in {}'
              .format(individual.id))
for family in families.values():
    if not user_story_42.is_date_valid(family):
        print('ERROR: FAMILY: US42: Invalid dates occurs in {}'
              .format(family.id))



file = open('./test_ged/user_story_39_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('\nTest user story 39: Upcoming Anniversaries of couples: ')
GedcomClass.main(file)
print('INFORMATION: FAMILY: US39: The list of anniversaries of couples is {}'
      .format(user_story_39.upcomingAnniversaries(families,individuals)))


file = open('./test_ged/user_story_33_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('\nTest user story 33: List of orphaned Children: ')
GedcomClass.main(file)
print('INFORMATION: INDIDIVUAL: US33: The list of orphans is {}'
      .format(user_story_33.recentOrphans(families,individuals)))