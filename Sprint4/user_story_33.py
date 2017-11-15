import GedcomClass
from datetime import datetime, timedelta

def recentOrphans(families,individuals):
    curr_date = datetime.today()
    before_30days = curr_date - timedelta(days=30)

    orphans_list =[]

    for family in families:
        check_family = GedcomClass.get_family(family, families)
        check_dad_alive = individuals.get(check_family.husb).alive
        check_mom_alive= individuals.get(check_family.wife).alive
        check_chil = check_family.chil_str

        if check_chil != 'NA':
            for chil in check_chil:
                chil_age = individuals.get(chil).age
                if(check_dad_alive == False and check_mom_alive == False and chil_age < 18):
                    orphans_list.append(chil)

    return orphans_list