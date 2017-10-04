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
        print('Error: INDIVIDUAL: {}: Birthday {} occurs in the future'.format(person, birt))
    if not UsersStories.dates_b4_current_indi(deat):
        print('Error: INDIVIDUAL: {}: Death {} occurs in the future'.format(person, deat))
    if not UsersStories.bir_deth(person, individuals):
        print('Error: INDIVIDUAL: {}: Birthday {} occurs after death {}'.format(person, birt, deat))
    if not UsersStories.age_less(person, individuals):
        print('Error: INDIVIDUAL: {} age is larger than 150'.format(person))

for family in families:
    marr = Gedcom.get_args(family, 'MARR', families)
    div = Gedcom.get_args(family, 'DIV', families)
    husb = Gedcom.get_args(family, 'HUSB', families)
    wife = Gedcom.get_args(family, 'WIFE', families)

    if not UsersStories.dates_b4_current_fam(marr):
        print('Error: FAMILY: {}: Marriage {} occurs in the future'.format(family, marr))
    if not UsersStories.bir_marriage(husb, family, individuals, families):
        print('Error: FAMILY: {}: Husband {} birthday {} occurs after marriage {}'.
              format(family, husb, Gedcom.get_args(husb, 'BIRT', individuals), marr))
    if not UsersStories.bir_marriage(wife, family, individuals, families):
        print('Error: FAMILY: {}: Wife {} birthday {} occurs after marriage {}'.
              format(family, wife, Gedcom.get_args(wife, 'BIRT', individuals), marr))
    if not UsersStories.is_marriage_before_divorce(family, families):
        print('Error: FAMILY: {}: Marriage {} occurs after divorce {}'.format(family, marr, div))
    if not UsersStories.is_marriage_before_death(husb, family, families, individuals):
        print('Error: FAMILY: {}: Husband {} death {} occurs before marriage {}'.
              format(family, husb, Gedcom.get_args(husb, 'DEAT', individuals), marr))
    if not UsersStories.is_marriage_before_death(wife, family, families, individuals):
        print('Error: FAMILY: {}: Wife {} death {} occurs before marriage {}'.
              format(family, wife, Gedcom.get_args(wife, 'DEAT', individuals), marr))
    if not UsersStories.div_b4_death(div,
                                     Gedcom.get_args(husb, 'DEAT', individuals),
                                     Gedcom.get_args(wife, 'DEAT', individuals)):
        print('Error: FAMILY: {}: Divorce {} occurs before death'.format(family, div))
