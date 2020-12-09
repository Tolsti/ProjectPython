def digital_root(n):
    return n%9


print(digital_root(16), 7)
print(digital_root(942), 6)
print(digital_root(132189), 6)
print(digital_root(493193), 2)
print(digital_root(195), 6)
print(digital_root(992), 2)
print(digital_root(999999999999), 9)
print(digital_root(167346), 9)
print(digital_root(10), 1)
print(digital_root(0), 0)

print(chr(1))