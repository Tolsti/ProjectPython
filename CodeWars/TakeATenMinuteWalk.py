def is_valid_walk(walk):
    n, s, e, w = 0, 0, 0, 0
    for i in walk:
        if i == 'n':
            n += 1
        if i == 's':
            s += 1
        if i == 'e':
            e += 1
        if i == 'w':
            w += 1
    return n == s and e == w and len(walk) == 10


print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']), 'should return True')
print(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']), 'should return False')
print(is_valid_walk(['w']), 'should return False')
print(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']), 'should return False')
