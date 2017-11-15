import GedcomClass
from Sprint1 import user_story_1
from Sprint1 import user_story_2
from Sprint1 import user_story_3
from Sprint1 import user_story_4
from Sprint1 import user_story_5
from Sprint1 import user_story_6
from Sprint1 import user_story_7
from Sprint1 import user_story_8
from Sprint2 import user_story_10
from Sprint2 import user_story_11
from Sprint2 import user_story_14
from Sprint2 import user_story_15
from Sprint2 import user_story_16
from Sprint2 import user_story_22
from Sprint2 import user_story_09
from Sprint2 import user_story_12
from Sprint3 import user_story_13
from Sprint3 import user_story_18
from Sprint3 import user_story_21
from Sprint3 import user_story_23
from Sprint3 import user_story_24
from Sprint3 import user_story_28
from Sprint3 import user_story_29
from Sprint3 import user_story_30
from Sprint4 import user_story_31
from Sprint4 import user_story_38
from Sprint4 import user_story_34
from Sprint4 import user_story_42
from Sprint4 import user_story_35
from Sprint4 import user_story_36
from Sprint4 import user_story_33
from Sprint4 import user_story_39

file = open('./Sprint1/test_ged/user_story_1_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
GedcomClass.main(file)
for person in individuals.values():
    birt = person.birt
    deat = person.deat
    if not user_story_1.dates_b4_current_indi(birt):
        print('Error: INDIVIDUAL: US01: {}: Birthday {} occurs in the future'.format(person.id, birt))
    if not user_story_1.dates_b4_current_indi(deat):
        print('Error: INDIVIDUAL: US01: {}: Death {} occurs in the future'.format(person.id, deat))

file = open('./Sprint1/test_ged/user_story_2_test.ged', 'r')
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

file = open('./Sprint1/test_ged/user_story_3_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
GedcomClass.main(file)
for person in individuals.values():
    if not user_story_3.bir_deth(person):
        print('Error: INDIVIDUAL: US03: {}: Birthday occurs after death'.format(person.id))

file = open('./Sprint1/test_ged/user_story_4_test.ged', 'r')
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for family in families.values():
    if not user_story_4.is_marriage_before_divorce(family):
        print('Error: FAMILY: US04: {}: Marriage occurs after divorce'.format(family.id))

file = open('./Sprint1/test_ged/user_story_5_test.ged', 'r')
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

file = open('./Sprint1/test_ged/user_story_6_test.ged', 'r')
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

file = open('./Sprint1/test_ged/user_story_7_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
GedcomClass.main(file)
for person in individuals.values():
    if not user_story_7.age_not_too_old(person):
        print('Error: INDIVIDUAL: US07: {} age is larger than 150'.format(person.id))

file = open('./Sprint1/test_ged/user_story_8_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for person in individuals.values():
    family_id = person.child_of
    if family_id != 'NA':
        if not user_story_8.birth_before_marriage(person, families.get(family_id)):
            print('Error: FAMILY: US08: {}: Child {} birthday occurs before marriage or after divorce'
                  .format(family_id, person.id))

file = open('./Test GEDCOM Files/JULIE GEDCOM.ged', 'r')
GedcomClass.main(file)
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
for person in individuals.values():
    spouses = person.spouse_of
    if spouses == 'NA':
        continue
    for spouse in spouses:
        if not user_story_10.marriage_after_14(person.birt, families.get(spouse).marr):
            print('Error: INDIVIDUAL: US010: {}: Marriage {} before 14 years old'
                  .format(person.id, families.get(spouse).marr_str))

for person in individuals:
    if not user_story_11.no_bigamy(person, individuals, families):
        print('Error: INDIVIDUAL: US011: {}: Marriage occurs during another marriage'
              .format(person))

file = open('./Sprint2/test_ged/user_story_14_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for family in families:
    if not user_story_14.has_more_than_five_birth(family, individuals, families):
        print('Error: FAMILY: US014: {}: has more than five siblings born at the same time'.format(family))

file = open('./Sprint2/test_ged/user_story_15_test.ged', 'r')
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for family in families:
    if not user_story_15.has_more_than_fifteen_siblings(family, families):
        print('Error: FAMILY: US015: {}: has more than 15 siblings'.format(family))

file = open('./Sprint2/test_ged/user_story_16_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for family in families:
    if not user_story_16.same_male_last_name(family, individuals, families):
        print('Error: FAMILY: US016: {}: Last names of male members are not the same'.format(family))

file = open('./Sprint2/test_ged/user_story_22_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for person in individuals:
    if not user_story_22.is_id_unique(person, individuals):
        print('Error: INDIVIDUAL: US022: {}: id is not unique'.format(person))
for family in families:
    if not user_story_22.is_id_unique(family, families):
        print('Error: FAMILY: US022: {}: id is not unique'.format(family))

file = open('./Sprint2/test_ged/user_story_9_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for child in individuals:
    if not user_story_09.birth_before_parents_death(child, individuals, families):
        print('Error: INDIVIDUAL: US09: {}: Child birth after parents death'.format(child))

file = open('./Sprint2/test_ged/user_story_12_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for child in individuals:
    if not user_story_12.parents_not_too_old(child, individuals, families):
        print('Error: INDIVIDUAL: US12: {}: Parents are too old when child birth'.format(child))

file = open('./Sprint3/test_ged/user_story_13_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('Test user story 13:')
GedcomClass.main(file)
for individual in individuals.values():
    family = GedcomClass.get_family(individual.child_of, families)
    if not user_story_13.siblings_spacing(individual, family, individuals):
        print('Error: FAMILY: US13: {}: Birth dates of siblings are more than 2 days and less than 8 months'
              .format(family.id))

file = open('./Sprint3/test_ged/user_story_18_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('\n Test user story 18:')
GedcomClass.main(file)
for family in families.values():
    if not user_story_18.siblings_not_married(family, individuals):
        print('Error: FAMILY: US18: {}: Siblings are married.'
              .format(family.id))

file = open('./Sprint3/test_ged/user_story_21_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('\n Test user story 21:')
GedcomClass.main(file)
for family in families.values():
    if not user_story_21.correct_gender(family, individuals):
        print('Error: FAMILY: US21: {}: Husband is not male or wife is not female'
              .format(family.id))

file = open('./Sprint3/test_ged/user_story_23_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
print('\n Test user story 23:')
GedcomClass.main(file)
for individual in individuals.values():
    if not user_story_23.uniqueNameAndBirth(individual, individuals):
        print('Error: INDIVIDUAL: US23: {}: Name and Birthday are not unique for the individual'
              .format(individual.id))

file = open('./Sprint3/test_ged/user_story_24_test.ged', 'r')
families = GedcomClass.read_families(file)
individuals = GedcomClass.read_individuals(file)
print('\n Test user story 24:')
GedcomClass.main(file)
for family in families.values():
    if not user_story_24.uniqueSpousesAndMarriage(family, families, individuals):
        print('Error: FAMILY: US24: {}: Spouse information and Marriage dates are not unique for this family'
              .format(family.id))

file = open('./Sprint3/test_ged/user_story_28_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('\n Test user story 28:')
GedcomClass.main(file)
for family in families.values():
    if user_story_28.order_siblings_by_age(family, individuals) == 'No children':
        print('Error: FAMILY: US28: {}: No children.'
              .format(family.id))
    elif user_story_28.order_siblings_by_age(family, individuals) == 'Only one child':
        print('Error: FAMILY: US28: {}: Only one child.'
              .format(family.id))
    else:
        print('FAMILY: US28: {} ordered oldest to youngest.'.format(
            user_story_28.order_siblings_by_age(family, individuals)))

file1 = open('./Sprint3/test_ged/user_story_29_test.ged', 'r')
file2 = open('./Sprint3/test_ged/user_story_29_test_2.ged', 'r')
individuals = GedcomClass.read_individuals(file1)
print('\n Test user story 29 No deceased:')
GedcomClass.main(file1)
if len(user_story_29.deceased_people(individuals)) == 0:
    print('Error: US29: No deceased')
else:
    print('INDIVIDUAL: US29: {}'.format(user_story_29.deceased_people(individuals)))

individuals = GedcomClass.read_individuals(file2)
print('\n Test user story 29 deceased:')
GedcomClass.main(file2)
if len(user_story_29.deceased_people(individuals)) == 0:
    print('Error: US29: No deceased')
else:
    print('INDIVIDUAL: US29: {}'.format(user_story_29.deceased_people(individuals)))

file = open('./Sprint3/test_ged/user_story_30_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('\n Test user story 30:')
GedcomClass.main(file)
print('INFORMATION: FAMILY: US30: The list of living married individuals is {}'
      .format(user_story_30.living_married(families, individuals)))

file = open('./Sprint4/test_ged/user_story_31_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
print('\nTest user story 31: Living Singles:')
GedcomClass.main(file)
if len(user_story_31.living_singles(individuals)) == 0:
    print('Error: US31: No Living Singles')
else:
    print('INFORMATION: INDIVIDUAL: US31: The list of living singles is {}'
          .format(user_story_31.living_singles(individuals)))

file = open('./Sprint4/test_ged/user_story_34_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('\nTest user story 34: Large Age Difference: ')
GedcomClass.main(file)
print('INFORMATION: FAMILY: US34: The list of large age difference couples is {}'
      .format(user_story_34.list_large_age_differences(individuals, families)))

file = open('./Sprint4/test_ged/user_story_35+36_test_1.ged', 'r')
individuals = GedcomClass.read_individuals(file)
print('\nTest user story 35: Recent Born: ')
GedcomClass.main(file)
if len(user_story_35.recently_born(individuals)) == 0:
    print('Error: US35: No Recent Born')
else:
    print('INFORMATION: INDIVIDUAL: US35: The recent born indivisuals are {}'
          .format(user_story_35.recently_born(individuals)))

file = open('./Sprint4/test_ged/user_story_35+36_test_1.ged', 'r')
individuals = GedcomClass.read_individuals(file)
print('\nTest user story 36: Recent Death: ')
GedcomClass.main(file)
if len(user_story_36.recently_dead(individuals)) == 0:
    print('Error: US31: No Recent Deaths')
else:
    print('INFORMATION: INDIVIDUAL: US36: The recent dead indivisuals are {}'
          .format(user_story_36.recently_dead(individuals)))

file = open('./Sprint4/test_ged/user_story_38_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
print('\nTest user story 38: Upcoming Birthdays: ')
GedcomClass.main(file)
print('INFORMATION: INDIVIDUAL: US38: The list of upcoming birthdays is {}'
      .format(user_story_38.upcoming_births(individuals)))

file = open('./Sprint4/test_ged/user_story_42_test.ged', 'r')
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

file = open('./Sprint4/test_ged/user_story_39_test.ged', 'r')
families = GedcomClass.read_families(file)
print('\nTest user story 39: Upcoming Anniversaries of couples: ')
GedcomClass.main(file)
print('INFORMATION: FAMILY: US39: The list of anniversaries of couples is {}'
      .format(user_story_39.upcoming_anniversaries(families)))

file = open('./Sprint4/test_ged/user_story_33_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
print('\nTest user story 33: List of orphaned Children: ')
GedcomClass.main(file)
print('INFORMATION: INDIDIVUAL: US33: The list of orphans is {}'
      .format(user_story_33.recent_orphans(families, individuals)))
