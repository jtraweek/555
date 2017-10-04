import Gedcom
from datetime import datetime


def bir_deth(person_id, individuals):
    # this method will compare between birth and date to find legit date format.
    b = Gedcom.get_args(person_id, 'BIRT', individuals)
    d = Gedcom.get_args(person_id, 'DEAT', individuals)

    if b == 'NA':
        return False
    b_date = datetime.strptime(b, '%d %b %Y')

    if d == 'NA':
        d_date = datetime.today()
    else:
        d_date = datetime.strptime(d, '%d %b %Y')

    if d_date >= b_date:
        return True
    return False


def bir_marriage(person_id, family_id, individuals, families):
    # this method will ensure that the birth date is before the marraige date.
    b = Gedcom.get_args(person_id, 'BIRT', individuals)
    m = Gedcom.get_args(family_id, 'MARR', families)

    if b == 'NA' or m == 'NA':
        return False
    b_date = datetime.strptime(b, '%d %b %Y')
    m_date = datetime.strptime(m, '%d %b %Y')

    if m_date >= b_date:
        return True
    return False
