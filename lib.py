def is_int(el):
    try:
        el = int(el)
    except ValueError:
        return False
    return True
