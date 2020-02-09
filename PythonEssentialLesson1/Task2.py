"""Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов.
Сделайте так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней."""


class Review:
    rating = None
    author = None
    review = None
    
    def __init__(self, rating, author, review):
        self.rating = rating
        self.author = author
        self.review = review
    
    def __str__(self):
        return '|Оценка: {}|\n'\
               '|Автор: {}|\n'\
               '|Отзыв: {}|'.format(self.rating, self.author, self.review)
