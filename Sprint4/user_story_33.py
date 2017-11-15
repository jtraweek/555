import GedcomClass
def recentOrphans(families, individuals):
    orphans_list = []

    for family in families.values():
        check_dad_alive = individuals.get(family.husb).alive
        check_mom_alive = individuals.get(family.wife).alive
        check_chil = family.chil

        if check_chil != []:
            for chil in check_chil:
                chil_age = GedcomClass.get_individual(chil, individuals).age
                if not check_dad_alive and not check_mom_alive and chil_age < 18:
                    orphans_list.append(chil)

    return orphans_list
