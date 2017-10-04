import Gedcom
from datetime import datetime


def dates_b4_current_indi(birth, death):
    """
    Checks birth, death dates to ensure they occurred before the current date
    """
    birth_date = datetime.strptime(birth, '%d %b %Y')
    if death != 'NA':
        death_date = datetime.strptime(death, '%d %b %Y')
        if birth_date.date() < datetime.today().date() and death_date.date() < datetime.today().date():
            return True
        else:
            return False

    if birth_date.date() < datetime.today().date():
        return True
    else:
        return False


def dates_b4_current_fam(marriage, divorce):
    """
    Checks marriage, divorce dates to ensure they occurred before current date
    """
    if marriage == 'NA' and divorce == 'NA':
        return True
    marriage_date = datetime.strptime(marriage, '%d %b %Y')

    if divorce != 'NA':
        divorce_date = datetime.strptime(divorce, '%d %b %Y')
        if marriage_date.date() < datetime.today().date() and divorce_date.date() < datetime.today().date():
            return True
        else:
            return False

    if marriage_date.date() < datetime.today().date():
        return True
    else:
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
        return False
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


def is_marriage_before_death(family_id, families, individuals):
    """
    User Story 5: Marriage before death
    Marriage should occur before death of either spouse
    :return: True on valid marriage date
    """
    marriage = Gedcom.get_args(family_id, 'MARR', families)

    # get death record of family
    husband = Gedcom.get_args(Gedcom.get_args(family_id, 'HUSB', families), 'DEAT', individuals)
    wife = Gedcom.get_args(Gedcom.get_args(family_id, 'WIFE', families), 'DEAT', individuals)

    if marriage == 'NA':
        return False
    marriage_date = datetime.strptime(marriage, '%d %b %Y')

    # if no death record found
    # set it today
    if husband == 'NA':
        husband_date = datetime.today()
    else:
        husband_date = datetime.strptime(husband, '%d %b %Y')
    if wife == 'NA':
        wife_date = datetime.today()
    else:
        wife_date = datetime.strptime(wife, '%d %b %Y')

    if husband_date >= marriage_date and wife_date >= marriage_date:
        return True
    return False


def div_b4_death(divorce, husb_death, wife_death):
    """
    Ensures divorce date occurred after death of husband & wife
    """
    if divorce == 'NA':
        div_b4_death = 'NO DIV'
        return div_b4_death
    elif husb_death == 'NA' and wife_death == 'NA':
        return True
    else:
        divorce_date = datetime.strptime(divorce, '%d %b %Y')
        husb_death_check, wife_death_check = True, True
        if husb_death != 'NA':
            husb_death_date = datetime.strptime(husb_death, '%d %b %Y')
            if divorce_date.date() > husb_death_date.date():
                husb_death_check = False

        if wife_death != 'NA':
            wife_death_date = datetime.strptime(wife_death, '%d %b %Y')
            if divorce_date.date() > wife_death_date.date():
                wife_death_check = False

        if husb_death_check == True and wife_death_check == True:
            return True
        else:
            return False
