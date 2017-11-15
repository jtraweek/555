import datetime
from datetime import timedelta


def upcomingAnniversaries(families, individuals):
    curr_date = datetime.datetime.today()
    after_30days = curr_date + timedelta(days=30)

    spouse_list = []

    for family in families.values():
        check_husb = individuals.get(family.husb).name
        check_wife = individuals.get(family.wife).name
        marr = family.marr
        if marr != 'NA':
            marr = marr.replace(year=curr_date.year)
            if curr_date <= marr <= after_30days:
                spouse_list.append("( " + check_husb + " " + check_wife + " )")

    return spouse_list
