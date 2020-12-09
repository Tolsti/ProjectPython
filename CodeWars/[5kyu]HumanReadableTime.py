def make_readable(seconds):
    h, m, s = 0, 0, seconds
    while s >= 60:
        s -= 60
        m += 1
        if m >= 60:
            m -= 60
            h += 1
    
    if len([sec for sec in str(h)]) == 1:
        h = '0' + str(h)
    if len([sec for sec in str(m)]) == 1:
        m = '0' + str(m)
    if len([sec for sec in str(s)]) == 1:
        s = '0' + str(s)
    
    return '{}:{}:{}'.format(h, m, s)
