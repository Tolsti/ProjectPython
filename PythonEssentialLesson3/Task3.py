"""Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год поступления на работу.
Конструктор должен генерировать исключение, если заданы неправильные данные. Введите список работников с клавиатуры.
Выведите всех сотрудников, которые были приняты после заданного года."""

import re


class Employee:
    def __init__(self, name=None, surname=None, department=None, year_of_employment=None):
        self._day = int(re.findall('\w\w', year_of_employment)[0])
        self._month = int(re.findall('\w\w', year_of_employment)[1])
        self._year = int(re.findall('\w\w', year_of_employment)[2] + re.findall('\w\w', year_of_employment)[3])
        
        if (name and surname and department and year_of_employment) is None:
            print('Введите данные сотрудника:')
            self.name = input('Имя: ')
            self.surname = input('Фамилия: ')
            self.department = input('Отдел: ')
            while True:
                try:
                    print('Дата поступления на работу:')
                    day = int(input('День: '))
                    month = int(input('Месяц: '))
                    year = int(input('Год: '))
                    if 1 <= day <= 31 and 1 <= month <= 12 and year <= 2020:
                        print()
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print()
                    print('Не верные параметры даты!')
                    print()
            self.year_of_employment = '{}.{}.{}'.format(day, month, year)
        
        else:
            self.name = name
            self.surname = surname
            self.department = department
            self.year_of_employment = year_of_employment
    
    def __repr__(self):
        return 'Данные о сотруднике:\n'\
               'Имя: %r\n'\
               'Фамилия: %r\n'\
               'Отдел: %r\n'\
               'Дата поступления на работу: %r\n' % (self.name, self.surname, self.department, self.year_of_employment)


class Company:
    def __init__(self):
        self._employee_list = list()
    
    def add_employee(self, name=None, surname=None, department=None, year_of_employment=None):
        if (name and surname and department and year_of_employment) is None:
            self._employee_list.append(Employee())
        else:
            self._employee_list.append(Employee(name, surname, department, year_of_employment))
    
    def search_for_employee_by_date(self, search_year=None):
        if search_year is None:
            search_year = int(input('Введите год сортировки: '))
        
        for i in self._employee_list:
            if search_year <= i._year:
                print(i)
    
    def __repr__(self):
        result = 'Все сотрудники:\n'
        for i in self._employee_list:
            result = result + str(i) + '\n'
        return result


company = Company()
company.add_employee('Николай', 'Фомин', 'Тех. поддержка', '12.06.2018')
company.add_employee('Анна', 'Филатова', 'Бухгалтерия', '30.07.2012')
company.add_employee('Лариса', 'Горная', 'Бухгалтерия', '24.01.2020')
# company.add_employee()

# print(company)
company.search_for_employee_by_date()
