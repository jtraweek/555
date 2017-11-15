import GedcomClass


def list_large_age_differences(individuals, families):
    _list = []
    for family in families.values():
        husb = GedcomClass.get_individual(family.husb, individuals)
        wife = GedcomClass.get_individual(family.wife, individuals)
        husb_birt = husb.birt
        wife_birt = wife.birt

        if husb_birt == 'NA' or wife_birt == 'NA' or family.marr == 'NA':
            continue

        marr_year = family.marr.year
        husb_age = marr_year - husb_birt.year
        wife_age = marr_year - wife_birt.year
        if husb_age / wife_age < 0.5 or husb_age / wife_age > 2:
            _list.append(family.id)

    return _list
