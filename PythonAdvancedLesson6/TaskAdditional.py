"""Создайте два класса Directory (папка) и File (файл).

Класс Directory должен иметь следующие поля:
- название (name типа str);
- родительская папка (root типа Directory);
- список файлов (files типа список, состоящий из экземпляров File)
- список подпапок (sub_directories типа список, состоящий из экземпляров Directory).

Класс Directory должен иметь следующие поля:
- добавление папки в список подпапок (add_sub_directory принимающий экземпляр Directory и
присваивающий поле root для принимаемого экземпляра);
- удаление папки из списка подпапок (remove_sub_directory,
принимающий экземпляр Directory и обнуляющий у него поле root. Метод также удаляет папку из списка sub_directories).
- добавление файла в папку (add_file, принимающий экземпляр File и
присваивающий ему поле directory - см. класс File ниже);
- удаление файла из папки (remove_file, принимающий экземпляр File и обнуляющий у него поле directory.
Метод удаляет файл из списка files).

Класс File должен иметь следующие поля: - название (name типа str); - папка (directory типа Directory);"""