def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    copy = lst[:]
    count = 0
    for i in range(len(lst)):
        if not lst[i]:
            del copy[i-count]
            count+=1
    
    return copy