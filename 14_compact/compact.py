def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    new_li = []
    for i in lst:
        if bool(i) == True:
            new_li.append(i)
    return new_li