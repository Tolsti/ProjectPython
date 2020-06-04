"""Создайте список товаров в интернет-магазине. Сериализуйте его при помощи pickle и сохраните в JSON."""

import json
import pickle


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_json(self):
        return {'name': self.name, 'price': self.price}

    def __repr__(self):
        return 'Product({!r}, {!r})'.format(self.name, self.price)


products = [Product('sofa', 500),
            Product('table', 300),
            Product('bed', 460),
            Product('mirror', 150),
            Product('chair', 50)]
print(products)

with open('data/product.pkl', 'wb') as data:
    pickle.dump(products, data)

with open('data/product.json', 'w') as data:
    with open('data/product.pkl', 'rb') as data_pkl:
        json.dump(pickle.load(data_pkl), data,
                  indent=2, default=Product.to_json)
