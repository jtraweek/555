import GedcomClass

def uniqueSpousesAndMarriage(fam, families, individuals):

    husb= individuals.get(fam.husb).name
    wife = individuals.get(fam.wife).name
    marriage = fam.marr_str

    count =0
    for family in families:
        check_family = GedcomClass.get_family(family, families)
        check_husb = individuals.get(check_family.husb).name
        check_wife = individuals.get(check_family.wife).name
        check_marr = check_family.marr_str

        if(check_husb == husb and check_wife  == wife and check_marr == marriage):
            count = count +1

    if (count <= 1):
        return True
    else:
        return False