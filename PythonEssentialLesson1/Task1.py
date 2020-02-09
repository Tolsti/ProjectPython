"""Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе издания и жанре.
Создайте несколько разных книг. Определите для него операции проверки на равенство и неравенство,
методы __repr__ и __str__."""
from Task2 import Review


class Book:
    
    def __init__(self, author, title, publication_date, genre):
        self.author = author
        self.title = title
        self.publication_date = publication_date
        self.genre = genre
        self.list_reviews = list()
    
    def set_review(self, rating, author, review):
        self.list_reviews.append(Review(rating, author, review))
    
    def show_book(self):
        print(self.author, self.title, self.publication_date, self.genre)
    
    def __eq__(self, other):
        return self.author == other.author and\
               self.title == other.title and\
               self.publication_date == other.publication_date and\
               self.genre == other.genre
    
    def __str__(self):
        reviews = '\n'
        if len(self.list_reviews) > 0:
            for i in self.list_reviews:
                reviews += str(i) + '\n'
        
        else:
            reviews += 'Нет отзывов\n'
        return 'Автор книги: {}\n'\
               'Название книги: {}\n'\
               'Дата издания: {}\n'\
               'Жанр: {}\n'\
               'Отзывы на книгу: {}'.format(self.author, self.title, self.publication_date, self.genre, reviews)


def main():
    book1 = Book('Шаман Иван', 'Валор', '2020.02.09', 'Фэнтези')
    book2 = Book('Федорочев Алексей', 'Начало', '2016.12.19', 'Фэнтези')
    book3 = Book('Делдерфилд Рональд Фредерик', 'Приключения Бена Ганна', '2015.04.07', 'Морские приключения')
    book4 = Book('Шаман Иван', 'Валор', '2020.02.09', 'Фэнтези')
    book5 = Book('Катя Вереск', 'Кошка для босса', '2017.11.24', 'Женский роман')
    
    book1.set_review(4, 'Ирина Морозова', 'Где же новые работы,автор?))')
    book5.set_review(5, 'Марьяна Дацык', 'Интересная книга. Оч неожиданно после истории Жени и Лины. '
                                         'Интригует и захватывает. Не думала,что Андрей окажется таким интересным и '
                                         'интригующим мужчиной. Ох!!!!')
    book5.set_review(4, 'Любовь Муравьева', 'Спасибо! Очень захватывающе!')
    book5.set_review(5, 'Анна Белозерова', 'Спасибо. Очень нравятся Ваши романы. Буду ждать новых.')
    
    # check on the validity
    if book1 == book4:
        print(True)
    
    print(book1)
    print(book2)
    print(book5)


if __name__ == '__main__':
    main()
