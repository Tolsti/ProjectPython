import string


def rot13(message):
    return message.translate(''.maketrans
                             ({**{x: y for x, y in zip(string.ascii_lowercase, (string.ascii_lowercase * 2)[13:])},
                               **{x: y for x, y in zip(string.ascii_uppercase, (string.ascii_uppercase * 2)[13:])}}))
