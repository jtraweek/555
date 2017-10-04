import Gedcom
from datetime import datetime


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
