def zeros(n):
    i, zero = 5, 0
    while n >= i:
        zero += n // i
        i *= 5
    return zero
