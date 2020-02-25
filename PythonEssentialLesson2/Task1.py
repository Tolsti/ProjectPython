"""Создайте класс Editor, который содержит методы view_document и edit_document. Пусть метод edit_document
выводит на экран информацию о том, что редактирование документов недоступно для бесплатной версии.
Создайте подкласс ProEditor, в котором данный метод будет переопределён. Введите с клавиатуры лицензионный ключ и,
если он корректный, создайте экземпляр класса ProEditor, иначе Editor.
Вызовите методы просмотра и редактирования документов."""


class Editor:
    _reg_key = ['1234', '4321', 'qwerty']

    def __init__(self, data_document):
        self.data_document = data_document

    def view_document(self):
        print(self.data_document)

    def edit_document(self):
        print('Редактирование документа не доступно для бесплатной версии.')


class ProEditor(Editor):
    def edit_document(self):
        # super().edit_document()
        print('Редактирование документа.')
        self.data_document = input('Введите данные нового документа: ')


if __name__ == '__main__':
    doc = 'Я помню чудное мгновенье:\n' \
          'Передо мной явилась ты,\n' \
          'Как мимолетное виденье,\n' \
          'Как гений чистой красоты.\n' \
          '\n' \
          'В томленьях грусти безнадежной,\n' \
          'В тревогах шумной суеты,\n' \
          'Звучал мне долго голос нежный\n' \
          'И снились милые черты.'
    if input('Введите ключ регистрации: ') in Editor._reg_key:
        print('У Вас платная версия.')
        document = ProEditor(doc)
    else:
        print('У Вас бесплатная версия.')
        document = Editor(doc)
    document.view_document()
    print('---------------------------')
    document.edit_document()
    print('---------------------------')

    document.view_document()
