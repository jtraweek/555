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
GedcomClass.main(file)
for individual in individuals.values():
    family = GedcomClass.get_family(individual.child_of, families)
    if not user_story_13.siblings_spacing(individual, family, individuals):
        print('Error: FAMILY: US13: {}: Birth dates of siblings are more than 2 days and less than 8 months'
              .format(family.id))

file = open('./test_ged/user_story_18_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)

file = open('./test_ged/user_story_21_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for family in families.values():
    if not user_story_21.correct_gender(family, individuals):
        print('Error: FAMILY: US21: {}: Husband is not male or wife is not female'
              .format(family.id))

file = open('./test_ged/user_story_23_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)

file = open('./test_ged/user_story_24_test.ged', 'r')
families = GedcomClass.read_families(file)
individuals = GedcomClass.read_individuals(file)

file = open('./test_ged/user_story_28_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)

file = open('./test_ged/user_story_29_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)

file = open('./test_ged/user_story_30_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
