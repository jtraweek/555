import Gedcom
from datetime import datetime
from dateutil.relativedelta import relativedelta


def dates_b4_current_indi(d):
    """
    Checks birth, death dates to ensure they occurred before the current date
    """
    if d != 'NA':
        date = datetime.strptime(d, '%d %b %Y')
        if date.date() < datetime.today().date():
            return True
        else:
            return False
    else:
        return True


def dates_b4_current_fam(d):
    """
    Checks marriage, divorce dates to ensure they occurred before current date
    """
    if d != 'NA':
        date = datetime.strptime(d, '%d %b %Y')
        if date.date() < datetime.today().date():
            return True
        else:
            return False
    else:
        return True


def bir_marriage(person_id, family_id, individuals, families):
    # this method will ensure that the birth date is before the marriage date.
    b = Gedcom.get_args(person_id, 'BIRT', individuals)
    m = Gedcom.get_args(family_id, 'MARR', families)

    if b == 'NA' or m == 'NA':
        return True
    b_date = datetime.strptime(b, '%d %b %Y')
    m_date = datetime.strptime(m, '%d %b %Y')

    if m_date >= b_date:
        return True
    return False


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


def is_marriage_before_divorce(family_id, families):
    """
    User Story 4: Marriage before divorce
    Marriage should occur before divorce of spouses, and divorce can only occur after marriage
    :return: True on valid marriage date
    """
    marriage = Gedcom.get_args(family_id, 'MARR', families)
    divorce = Gedcom.get_args(family_id, 'DIV', families)

    if marriage == 'NA':
        return True
    marriage_date = datetime.strptime(marriage, '%d %b %Y')

    # if no divorce record found
    # set it today
    if divorce == 'NA':
        divorce_date = datetime.today()
    else:
        divorce_date = datetime.strptime(divorce, '%d %b %Y')

    if divorce_date >= marriage_date:
        return True
    return False


def is_marriage_before_death(person_id, family_id, families, individuals):
    """
    User Story 5: Marriage before death
    Marriage should occur before death of either spouse
    :return: True on valid marriage date
    """
    marriage = Gedcom.get_args(family_id, 'MARR', families)

    # get death record of family
    deat = Gedcom.get_args(person_id, 'DEAT', individuals)

    if marriage == 'NA':
        return True
    marriage_date = datetime.strptime(marriage, '%d %b %Y')

    # if no death record found
    # set it today
    if deat == 'NA':
        date = datetime.today()
    else:
        date = datetime.strptime(deat, '%d %b %Y')

    if date >= marriage_date:
        return True
    return False


def div_b4_death(divorce, death):
    """
    Ensures divorce date occurred after death of husband & wife
    """
    if divorce == 'NA' or death == 'NA':
        return True
    else:
        divorce_date = datetime.strptime(divorce, '%d %b %Y')
        death_date = datetime.strptime(death, '%d %b %Y')
        if divorce_date.date() > death_date.date():
            return False
    return True


def age_less(person_id, individuals):
    if Gedcom.get_age(person_id, individuals) == 'NA':
        return False
    return True


def child_birth_after_marriage(marr, child_birth):
    """
    This function checks if a child is born before the marriage of their parents
    """
    if marr == 'NA' or child_birth == 'NA':
        return True
    else:
        marriage_date = datetime.strptime(marr, '%d %b %Y')
        child_birth_date = datetime.strptime(child_birth, '%d %b %Y')
        if child_birth_date.date() < marriage_date.date():
            return False
    return True


def child_birth_before_divorce(div, child_birth):
    """
    This function checks if a child is born before the marriage of their parents
    """
    if div == 'NA' or child_birth == 'NA':
        return True
    else:
        divorce_date = datetime.strptime(div, '%d %b %Y')
        divorce_date_after_nine = divorce_date + relativedelta(months=9)
        child_birth_date = datetime.strptime(child_birth, '%d %b %Y')
        if child_birth_date.date() > divorce_date_after_nine.date():
            return False
    return True
