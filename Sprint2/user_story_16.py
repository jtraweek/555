def same_male_last_name(fimily_id, individuals, families):
    family = families.get(fimily_id)
    father_name = individuals.get(family.husb).name
    if father_name == 'NA':
        return True
    father_names = father_name.split()

    for child_id in family.chil:
        child = individuals.get(child_id)
        if child.sex == 'M':
            child_names = child.name.split()
            if child_names[-1] != father_names[-1]:
                return False
    return True
