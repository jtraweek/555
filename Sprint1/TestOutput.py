import Gedcom
from Spring1 import UsersStories

file = open('../Test GEDCOM Files/Liu ged.ged', 'r')
Gedcom.main(file)
families = Gedcom.read_families(file)
individuals = Gedcom.read_individuals(file)

for person in individuals:

    birt = Gedcom.get_args(person, 'BIRT', individuals)
    deat = Gedcom.get_args(person, 'DEAT', individuals)

    if not UsersStories.dates_b4_current_indi(birt):
        print('Error: INDIVIDUAL: US01: {}: Birthday {} occurs in the future'.format(person, birt))
    if not UsersStories.dates_b4_current_indi(deat):
        print('Error: INDIVIDUAL: US01: {}: Death {} occurs in the future'.format(person, deat))
    if not UsersStories.bir_deth(person, individuals):
        print('Error: INDIVIDUAL: US03: {}: Birthday {} occurs after death {}'.format(person, birt, deat))
    if not UsersStories.age_less(person, individuals):
        print('Error: INDIVIDUAL: US07: {} age is larger than 150'.format(person))

for family in families:
    marr = Gedcom.get_args(family, 'MARR', families)
    div = Gedcom.get_args(family, 'DIV', families)
    husb = Gedcom.get_args(family, 'HUSB', families)
    wife = Gedcom.get_args(family, 'WIFE', families)

    if not UsersStories.dates_b4_current_fam(marr):
        print('Error: FAMILY: US01: {}: Marriage {} occurs in the future'.format(family, marr))
    if not UsersStories.dates_b4_current_fam(div):
        print('Error: FAMILY: US01: {}: Divorce {} occurs in the future'.format(family, div))
    if not UsersStories.bir_marriage(husb, family, individuals, families):
        print('Error: FAMILY: US02: {}: Husband {} birthday {} occurs after marriage {}'.
              format(family, husb, Gedcom.get_args(husb, 'BIRT', individuals), marr))
    if not UsersStories.bir_marriage(wife, family, individuals, families):
        print('Error: FAMILY: US02: {}: Wife {} birthday {} occurs after marriage {}'.
              format(family, wife, Gedcom.get_args(wife, 'BIRT', individuals), marr))
    if not UsersStories.is_marriage_before_divorce(family, families):
        print('Error: FAMILY: US04: {}: Marriage {} occurs after divorce {}'.format(family, marr, div))
    if not UsersStories.is_marriage_before_death(husb, family, families, individuals):
        print('Error: FAMILY: US05: {}: Husband {} death {} occurs before marriage {}'.
              format(family, husb, Gedcom.get_args(husb, 'DEAT', individuals), marr))
    if not UsersStories.is_marriage_before_death(wife, family, families, individuals):
        print('Error: FAMILY: US05: {}: Wife {} death {} occurs before marriage {}'.
              format(family, wife, Gedcom.get_args(wife, 'DEAT', individuals), marr))
    if not UsersStories.div_b4_death(div, Gedcom.get_args(husb, 'DEAT', individuals)):
        print('Error: FAMILY: US06: {}: Divorce {} occurs after husband {} death {}'
              .format(family, div, husb, Gedcom.get_args(husb, 'DEAT', individuals)))
    if not UsersStories.div_b4_death(div, Gedcom.get_args(wife, 'DEAT', individuals)):
        print('Error: FAMILY: US06: {}: Divorce {} occurs after wife {} death {}'
              .format(family, div, husb, Gedcom.get_args(wife, 'DEAT', individuals)))

    for child in Gedcom.get_args(family, 'CHIL', families):
        child_birth = Gedcom.get_args(child, 'BIRT', individuals)
        if not UsersStories.child_birth_after_marriage(marr, child_birth):
            print('Error: FAMILY: US08: {}: Child {} birthday {} occurs before marriage {}'
                  .format(family, child, child_birth, marr))
        if not UsersStories.child_birth_before_divorce(div, child_birth):
            print('Error: FAMILY: US08: {}: Child {} birthday {} occurs after nine months of divorce {}'
                  .format(family, child, child_birth, div))
