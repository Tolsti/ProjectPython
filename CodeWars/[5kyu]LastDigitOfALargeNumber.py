import math


def module(a, b):
    mod = 0
    
    for i in range(0, len(b)):
        mod = (mod * 10 + int(b[i])) % a
    
    return mod


def last_digit(n1, n2):
    n1 = [i for i in str(n1)]
    n2 = [i for i in str(n2)]
    
    if len(n1) == 1 and len(n2) == 1 and n2[0] == '0' and n1[0] == '0':
        return 1
    if len(n2) == 1 and n2[0] == '0':
        return 1
    if len(n1) == 1 and n1[0] == '0':
        return 0
    
    if module(4, n2) == 0:
        exp = 4
    else:
        exp = module(4, n2)
    
    res = math.pow(int(n1[len(n1) - 1]), exp)
    
    return int(res % 10)
