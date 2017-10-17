def has_more_than_five_birth(family_id, individuals, families):
    family = families.get(family_id)
    if family.chil == 'NA':
        return False
    dic = {}
    for child_id in family.chil:
        child = individuals.get(child_id)
        dic[child.birt_str] = dic.get(child.birt_str, 0) + 1
    for count in dic.values():
        if count > 5:
            return True
    return False
