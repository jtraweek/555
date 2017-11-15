from datetime import datetime
from datetime import timedelta


def upcoming_anniversaries(families):
    curr_date = datetime.today()
    after_30days = curr_date + timedelta(days=30)

    spouse_list = []
    for family in families.values():
        marr = family.marr
        if marr != 'NA':
            marr = marr.replace(year=curr_date.year)
            if curr_date <= marr <= after_30days:
                spouse_list.append(family.id)
    return spouse_list
