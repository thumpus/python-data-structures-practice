def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    is_list = True
    for i in lst:
        if isinstance(i, list) == False:
            is_list = False
    return is_list