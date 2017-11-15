def is_id_unique(_id, _set):
    if _set.get(_id).id_count > 1:
        return False
    return True
