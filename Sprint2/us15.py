def has_more_than_fifteen_siblings(family_id, families):
    family = families.get(family_id)
    if len(family.child) < 15:
        return True
    return False
