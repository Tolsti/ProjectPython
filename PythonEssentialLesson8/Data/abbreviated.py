import random
import shelve
import string


def abbreviated_link():
    while True:
        abbreviate_link = 'link.com/' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4))

        with shelve.open('data/list_of_links') as data:
            if abbreviate_link not in data.values():
                return abbreviate_link
