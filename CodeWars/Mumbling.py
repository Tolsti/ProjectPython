def accum(s):

    return '-'.join([s[r].upper()[0] + s[r].lower() * r for r in range(len(s))])
