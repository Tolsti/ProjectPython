def narcissistic(value):
    return value == sum([int(v) ** len(str(value)) for v in str(value)])
