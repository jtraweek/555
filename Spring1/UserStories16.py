import datetime


def dates_b4_current_indi(birth, death):
    """
    Checks birth, death dates to ensure they occurred before the current date
    """
    birth_date = datetime.datetime.strptime(birth, '%d %b %Y')
    if death != 'NA':
        death_date = datetime.datetime.strptime(death, '%d %b %Y')
        if birth_date.date() < datetime.datetime.today().date() and death_date.date() < datetime.datetime.today().date():
            return True
        else:
            return False

    if birth_date.date() < datetime.datetime.today().date():
        return True
    else:
        return False


def dates_b4_current_fam(marriage, divorce):
    """
    Checks marriage, divorce dates to ensure they occurred before current date
    """
    if marriage == 'NA' and divorce == 'NA':
        return True
    marriage_date = datetime.datetime.strptime(marriage, '%d %b %Y')

    if divorce != 'NA':
        divorce_date = datetime.datetime.strptime(divorce, '%d %b %Y')
        if marriage_date.date() < datetime.datetime.today().date() and divorce_date.date() < datetime.datetime.today().date():
            return True
        else:
            return False

    if marriage_date.date() < datetime.datetime.today().date():
        return True
    else:
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
        divorce_date = datetime.datetime.strptime(divorce, '%d %b %Y')
        husb_death_check, wife_death_check = True, True
        if husb_death != 'NA':
            husb_death_date = datetime.datetime.strptime(husb_death, '%d %b %Y')
            if divorce_date.date() > husb_death_date.date():
                husb_death_check = False

        if wife_death != 'NA':
            wife_death_date = datetime.datetime.strptime(wife_death, '%d %b %Y')
            if divorce_date.date() > wife_death_date.date():
                wife_death_check = False

        if husb_death_check == True and wife_death_check == True:
            return True
        else:
            return False
