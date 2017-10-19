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
    husb_id = family.husb
    wife_id = family.wife
    if husb_id != 'NA':
        if not user_story_2.bir_marriage(individuals.get(husb_id), family):
            print('Error: FAMILY: US02: {}: Husband {} birthday occurs after marriage'
                  .format(family.id, husb_id))
    if wife_id != 'NA':
        if not user_story_2.bir_marriage(individuals.get(wife_id), family):
            print('Error: FAMILY: US02: {}: Wife {} birthday occurs after marriage'
                  .format(family.id, wife_id))

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

file = open('./user_story_5_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for family in families.values():
    husb_id = family.husb
    wife_id = family.wife
    if husb_id != 'NA':
        if not user_story_5.is_marriage_before_death(individuals.get(husb_id), family):
            print('Error: FAMILY: US05: {}: Husband {} death occurs before marriage '.
                  format(family.id, husb_id))
    if wife_id != 'NA':
        if not user_story_5.is_marriage_before_death(individuals.get(wife_id), family):
            print('Error: FAMILY: US05: {}: Wife {} death occurs before marriage'.
                  format(family.id, wife_id))

file = open('./user_story_6_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for family in families.values():
    husb_id = family.husb
    wife_id = family.wife
    if husb_id != 'NA':
        if not user_story_6.div_b4_death(individuals.get(husb_id), family):
            print('Error: FAMILY: US06: {}: Divorce occurs after husband {} death'
                  .format(family.id, husb_id))
    if wife_id != 'NA':
        if not user_story_6.div_b4_death(individuals.get(wife_id), family):
            print('Error: FAMILY: US06: {}: Divorce occurs after wife {} death'
                  .format(family.id, wife_id))

file = open('./user_story_7_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
GedcomClass.main(file)
for person in individuals.values():
    if not user_story_7.age_not_too_old(person):
        print('Error: INDIVIDUAL: US07: {} age is larger than 150'.format(person.id))

file = open('./user_story_8_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for person in individuals.values():
    family_id = person.child
    if family_id != 'NA':
        if not user_story_8.birth_before_marriage(person, families.get(family_id)):
            print('Error: FAMILY: US08: {}: Child {} birthday occurs before marriage or after divorce'
                  .format(family_id, person.id))
