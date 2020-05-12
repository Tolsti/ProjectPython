"""Ознакомьтесь при помощи документации с классами namedtuple и deque модуля collections."""

import collections
import string

parts = collections.namedtuple('Parts', 'id_num desk cost amount')

auto_parts = parts(id_num='4352',
                   desk='Skoda Superb',
                   cost=8900,
                   amount=1)
print(*auto_parts)
for part in auto_parts:
    print(part)
print(auto_parts.id_num)

#######################################################################################################################

d = collections.deque(string.ascii_lowercase)
print(*d)

d.append('bork')
print(*d)

d.appendleft('test')
print(*d)

d.rotate(5)
print(*d)
