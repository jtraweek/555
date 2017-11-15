def has_more_than_fifteen_siblings(family_id, families):
    family = families.get(family_id)
    if len(family.chil) < 15:
        return False
    return True
