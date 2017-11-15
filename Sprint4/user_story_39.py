import GedcomClass
from datetime import datetime
from datetime import timedelta


def upcomingAnniversaries(families,individuals):
    curr_date = datetime.today()
    after_30days = curr_date + timedelta(days=30)

    spouse_list =[]

    for family in families:
        check_family = GedcomClass.get_family(family, families)
        check_husb = individuals.get(check_family.husb).name
        check_wife = individuals.get(check_family.wife).name
        check_marr = check_family.marr
        #marr_day = int(check_marr.day)
        #marr_month = int(check_marr.month)
        #this_year = int(datetime.date.year)
        #this_marr = datetime.date(this_year,marr_month, marr_day)
        if check_marr != 'NA':
            if curr_date < check_marr < after_30days:
                spouse_list.append(curr_date)

    return spouse_list