import Gedcom
from Spring1 import UsersStories

file = open('../Test GEDCOM Files/Liu ged.ged', 'r')
Gedcom.main(file)
families = Gedcom.read_families(file)
individuals = Gedcom.read_individuals(file)

for person in individuals:
    if not UsersStories.dates_b4_current_indi(Gedcom.get_args(person, 'BIRT', individuals),
                                              Gedcom.get_args(person, 'DEAT', individuals)):
        print('Error: INDIVIDUAL: {} occurs in the future'.format(person))
for family in families:
    if not UsersStories.is_marriage_before_divorce(family, families):
        print('Error: FAMILY: {} married before divorce'.format(family))
    if not UsersStories.is_marriage_before_death(family, families, individuals):
        print('Error: FAMILY: {} married before death'.format(family))
