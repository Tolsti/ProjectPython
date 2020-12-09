def disemvowel(string):
    for s in string:
        if s in 'AaEeIiUuOo':
            string = string.replace(s, '')
    return string
