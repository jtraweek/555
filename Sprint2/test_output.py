import GedcomClass
from Sprint2 import user_story_10
from Sprint2 import user_story_11
from Sprint2 import us14
from Sprint2 import us15
from Sprint2 import us16
from Sprint2 import us22
from Sprint2 import user_story_09
from Sprint2 import user_story_12

file = open('../Test GEDCOM Files/JULIE GEDCOM.ged', 'r')
GedcomClass.main(file)
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
for person in individuals.values():
    spouses = person.spouse
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

file = open('./us14_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for family in families:
    if not us14.has_more_than_five_birth(family, individuals, families):
        print('Error: FAMILY: US014: {}: has more than five siblings born at the same time'.format(family))

file = open('./us15_test.ged', 'r')
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for family in families:
    if not us15.has_more_than_fifteen_siblings(family, families):
        print('Error: FAMILY: US015: {}: has more than 15 siblings'.format(family))

file = open('./us16_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for family in families:
    if not us16.same_male_last_name(family, individuals, families):
        print('Error: FAMILY: US016: {}: Last names of male members are not the same'.format(family))

file = open('./us22_test.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
GedcomClass.main(file)
for person in individuals:
    if not us22.is_id_unique(person, individuals):
        print('Error: INDIVIDUAL: US022: {}: id is not unique'.format(person))
for family in families:
    if not us22.is_id_unique(family, families):
        print('Error: FAMILY: US022: {}: id is not unique'.format(family))

file = open('./us09_us12.ged', 'r')
individuals = GedcomClass.read_individuals(file)
families = GedcomClass.read_families(file)
GedcomClass.main(file)
dic = {}

for family in families.values():
    children_list = family.chil_str
    if children_list == 'NA':
        continue
    for child in children_list:
        if not user_story_09.birth_before_parents_death(family.id, child, individuals, families):
            dic['Error: INDIVIDUAL: US09: {}: Not born before parent death'.format(family.id)] = ''

for family in families.values():
    children_list = family.chil_str
    if children_list == 'NA':
        continue
    for child in children_list:
        if not user_story_12.parents_not_too_old(family.id, child, individuals, families):
            dic['Error: INDIVIDUAL: US12: {}: Parents are too old when child birth'.format(family.id)] = ''
for line in dic:
    print(line)
