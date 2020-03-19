"""Выучите основные стандартные исключения, которые перечислены в данном уроке."""

# базовое исключение, от которого берут начало все остальные.
raise BaseException

# исключение, порождаемое функцией sys.exit при выходе из программы.
raise SystemExit

# порождается при прерывании программы пользователем (обычно сочетанием клавиш Ctrl+C).
raise KeyboardInterrupt

# порождается при вызове метода close объекта generator.
raise GeneratorExit

# а вот тут уже заканчиваются полностью системные исключения (которые лучше не трогать)
# и начинаются обыкновенные, с которыми можно работать.
raise Exception

# порождается встроенной функцией next, если в итераторе больше нет элементов.
raise StopIteration

# арифметическая ошибка.
raise ArithmeticError

# порождается при неудачном выполнении операции с плавающей запятой. На практике встречается нечасто.
raise FloatingPointError

# возникает, когда результат арифметической операции слишком велик для представления.
# Не появляется при обычной работе с целыми числами (так как python поддерживает длинные числа),
# но может возникать в некоторых других случаях.
raise OverflowError

# деление на ноль.
raise ZeroDivisionError

# выражение в функции assert ложно.
raise AssertionError

# объект не имеет данного атрибута (значения или метода).
raise AttributeError

# операция, связанная с буфером, не может быть выполнена.
raise BufferError

# функция наткнулась на конец файла и не смогла прочитать то, что хотела.
raise EOFError

# не удалось импортирование модуля или его атрибута.
raise ImportError

# некорректный индекс или ключ.
raise LookupError

# индекс не входит в диапазон элементов.
raise IndexError

# несуществующий ключ (в словаре, множестве или другом объекте).
raise KeyError

# недостаточно памяти.
raise MemoryError

# не найдено переменной с таким именем.
raise NameError

# сделана ссылка на локальную переменную в функции, но переменная не определена ранее.
raise UnboundLocalError

# ошибка, связанная с системой.
raise OSError

raise BlockingIOError

# неудача при операции с дочерним процессом.
raise ChildProcessError

# базовый класс для исключений, связанных с подключениями.
raise ConnectionError

raise BrokenPipeError

raise ConnectionAbortedError

raise ConnectionRefusedError

raise ConnectionResetError

# попытка создания файла или директории, которая уже существует.
raise FileExistsError

# файл или директория не существует.
raise FileNotFoundError

# системный вызов прерван входящим сигналом.
raise InterruptedError

# ожидался файл, но это директория.
raise IsADirectoryError

# ожидалась директория, но это файл.
raise NotADirectoryError

# не хватает прав доступа.
raise PermissionError

# указанного процесса не существует.
raise ProcessLookupError

# закончилось время ожидания.
raise TimeoutError

# попытка доступа к атрибуту со слабой ссылкой.
raise ReferenceError

# возникает, когда исключение не попадает ни под одну из других категорий.
raise RuntimeError

# возникает, когда абстрактные методы класса требуют переопределения в дочерних классах.
raise NotImplementedError

# синтаксическая ошибка.
raise SyntaxError

# неправильные отступы.
raise IndentationError

# смешивание в отступах табуляции и пробелов.
raise TabError

# внутренняя ошибка.
raise SystemError

# операция применена к объекту несоответствующего типа.
raise TypeError

# функция получает аргумент правильного типа, но некорректного значения.
raise ValueError

# ошибка, связанная с кодированием / раскодированием unicode в строках.
raise UnicodeError

# исключение, связанное с кодированием unicode.
raise UnicodeEncodeError

# исключение, связанное с декодированием unicode.
raise UnicodeDecodeError

# исключение, связанное с переводом unicode.
raise UnicodeTranslateError

# предупреждение.
raise Warning
