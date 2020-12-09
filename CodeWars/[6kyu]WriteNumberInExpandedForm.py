def expanded_form(num):
    return ' + '.join([e + ('0' * (len(str(num)) - i - 1)) for i, e in enumerate(str(num)) if int(e) > 0])
