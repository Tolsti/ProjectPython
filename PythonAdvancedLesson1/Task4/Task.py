"""Изучите основные понятия, рассмотренные в уроке и работу с HTTP протоколам в Python,
используя библиотеки urllib и requests."""

import urllib.parse
import urllib.request

url = urllib.request.urlopen('https://www.mail.ru')
data = {'s': "Веб программирование"}
enc_data = urllib.parse.urlencode(data)

print('result code:', url.getcode())

print(url.read()[:350].decode('utf-8'))

print(url.info())

# GET запрос
f = urllib.request.urlopen("http://mail.ru/" + "?" + enc_data)
print(f.read())

# POST запрос
f = urllib.request.urlopen("http://mail.ru/", enc_data.encode('utf-8'))
print(f.read())

data_parse = [('n', '1'), ('n', '3'), ('n', '4'), ('button', 'Привет'), ]
enc_data_parse = urllib.parse.urlencode(data_parse)
print(enc_data_parse)

# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #

import requests

r = requests.get('https://api.github.com', auth=('user', 'pass'))

print(r.status_code)
print(r.headers['content-type'])

s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)

print(s.cookies.get_dict())

r = s.get('http://httpbin.org/cookies')
print(r.text)
