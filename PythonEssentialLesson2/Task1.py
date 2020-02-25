"""Создайте класс Editor, который содержит методы view_document и edit_document. Пусть метод edit_document
выводит на экран информацию о том, что редактирование документов недоступно для бесплатной версии.
Создайте подкласс ProEditor, в котором данный метод будет переопределён. Введите с клавиатуры лицензионный ключ и,
если он корректный, создайте экземпляр класса ProEditor, иначе Editor.
Вызовите методы просмотра и редактирования документов."""


class Editor:
    _reg_key = [1234, 4321, 'qwer']
    
    def __init__(self):
        self.data_document = 'Я помню чудное мгновенье:\n'\
                             'Передо мной явилась ты,\n'\
                             'Как мимолетное виденье,\n'\
                             'Как гений чистой красоты.\n'\
                             '\n'\
                             'В томленьях грусти безнадежной,\n'\
                             'В тревогах шумной суеты,\n'\
                             'Звучал мне долго голос нежный\n'\
                             'И снились милые черты.'
    
    def view_document(self):
        print(self.data_document)
    
    def edit_document(self):
        print('Редактирование документа не доступно для бесплатной версии.')


class ProEditor(Editor):
    def edit_document(self):
        super().edit_document()


if __name__ == '__main__':
    document = ProEditor()
    # document.view_document()
    document.edit_document()
