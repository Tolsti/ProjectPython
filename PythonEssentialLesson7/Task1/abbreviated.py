import random
import string

dictionary_links = {'vk.com': None, 'mail.ru': None, 'google.com': None, 'yandex.ru': None}


def abbreviated_link():
    while True:
        abbreviate_link = 'link.com/' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4))
        
        if abbreviate_link not in [_ for _ in dictionary_links.values()]:
            return abbreviate_link


for i in dictionary_links:
    dictionary_links[i] = abbreviated_link()

if __name__ == '__main__':
    print(dictionary_links)
