def unique_in_order(iterable):
    result, tmp = list(), None
    for i in iterable:
        if i != tmp:
            result.append(i)
        tmp = i
    return result
