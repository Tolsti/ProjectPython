"""Ознакомьтесь при помощи документации с классами OrderedDict, defaultdict и ChainMap модуля collections."""

import collections

# OrderedDict
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
d = collections.OrderedDict(sorted(d.items(), key = lambda t: t[0]))
print(d)
d = collections.OrderedDict(sorted(d.items(), key = lambda t: t[1]))
print(d)
d = collections.OrderedDict(sorted(d.items(), key = lambda t: len(t[0])))
print(d)
d.move_to_end('apple')
print(d)
d.popitem()
print(d)

# defaultdict
defdict = collections.defaultdict(list)
print(defdict)
for i in range(5):
    defdict[i].append(i)
print(defdict)

# ChainMap
car_parts = {'hood': 500, 'engine': 5000, 'front_door': 750}
car_options = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
car_accessories = {'cover': 100, 'hood_ornament': 150, 'seat_cover': 99}
car_pricing = collections.ChainMap(car_parts, car_options, car_accessories)
print(car_pricing)
