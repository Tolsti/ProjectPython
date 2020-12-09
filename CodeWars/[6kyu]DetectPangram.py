import string


def is_pangram(s):
    t_string = list()
    for index, i_s in enumerate(s.lower()):
        if i_s in string.ascii_lowercase and i_s not in t_string:
            t_string.append(i_s)
    if ''.join(sorted(t_string)) == string.ascii_lowercase:
        return True
    else:
        return False
