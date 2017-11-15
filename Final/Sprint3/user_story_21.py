import GedcomClass


def correct_gender(family, individuals):
    husb = GedcomClass.get_individual(family.husb, individuals)
    wife = GedcomClass.get_individual(family.wife, individuals)
    return (husb.sex == 'M' or husb.sex == 'NA') and (wife.sex == 'F' or wife.sex == 'NA')
