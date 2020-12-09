def rgb(r, g, b):
    return ''.join(['0' + str(hex(i))[2:].upper() if len(set(str(i))) == 1 else str(hex(i))[2:].upper()
                    for i in (i if i > 0 else 0 for i in (i if i < 255 else 255 for i in (r, g, b)))])
