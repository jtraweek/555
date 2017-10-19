import GedcomClass
from Sprint1 import user_story_1
from Sprint1 import user_story_2
from Sprint1 import user_story_3
from Sprint1 import user_story_4
from Sprint1 import user_story_5
from Sprint1 import user_story_6
from Sprint1 import user_story_7
from Sprint1 import user_story_8

file = open('./user_story_1_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
GedcomClass.main(file)
for person in individuals.values():
    birt = person.birt
    deat = person.deat
    if not user_story_1.dates_b4_current_indi(birt):
        print('Error: INDIVIDUAL: US01: {}: Birthday {} occurs in the future'.format(person.id, birt))
    if not user_story_1.dates_b4_current_indi(deat):
        print('Error: INDIVIDUAL: US01: {}: Death {} occurs in the future'.format(person.id, deat))

file = open('./user_story_2_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for family in families.values():
    husb = family.husb
    wife = family.wife
    if husb != 'NA':
        if not user_story_2.bir_marriage(individuals.get(husb), family):
            print('Error: FAMILY: US02: {}: Husband {} birthday occurs after marriage'
                  .format(family.id, husb))
    if wife != 'NA':
        if not user_story_2.bir_marriage(individuals.get(wife), family):
            print('Error: FAMILY: US02: {}: Wife {} birthday occurs after marriage'
                  .format(family.id, wife))

file = open('./user_story_3_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
GedcomClass.main(file)
for person in individuals.values():
    if not user_story_3.bir_deth(person):
        print('Error: INDIVIDUAL: US03: {}: Birthday occurs after death'.format(person.id))

file = open('./user_story_4_test.ged', 'r')
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for family in families.values():
    if not user_story_4.is_marriage_before_divorce(family):
        print('Error: FAMILY: US04: {}: Marriage occurs after divorce'.format(family.id))
