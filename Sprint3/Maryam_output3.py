import GedcomClass
from Sprint2 import user_story_10
from Sprint2 import user_story_11
from Sprint2 import user_story_14
from Sprint2 import user_story_15
from Sprint2 import user_story_16
from Sprint2 import user_story_22
from Sprint2 import user_story_09
from Sprint2 import user_story_12

# THIS FILE IS ADDRESSING WHAT EACH FEATURE SHOULD RETURN!
file = open('./test_ged/user_story_29_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for indi in individuals:
    if not US_29.deceased_people(individuals):
        print('Error: {}: is empty'.format([]))

file = open('./test_ged/user_story_30_test.ged', 'r')
families = GedcomClass.read_families(file)
individuals = GedcomClass.read_individuals(file)
GedcomClass.main(file)
for family in families.values():
    if family.div_str != 'NA':
        print('Error:{}: is single '.format(family.id))
    if family.husb.alive or family.wife.alive == 'NO':
        print('Error:{}: is dead '.format(family.husb))
        print('Error:{}: is dead '.format(family.wife))

    if not US_30.living_married(families, individuals):
        print('Error: {}: is empty'.format([]))

