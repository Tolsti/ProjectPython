# raise ValueError('invalid argument')

# print('Calculator')
#
# try:
#     a = float(input('a = '))
#     b = float(input('b = '))
#     print(a / b)
# except (ZeroDivisionError, ValueError)as error:
#     print(error)
#
# print('Stopping the calculator.')

# def main():
#     while True:
#         try:
#             first_number = float(input('First number: '))
#             second_number = float(input('Second number: '))
#             print('Result:', first_number / second_number)
#             break
#         except (ValueError, ZeroDivisionError)as error:
#             print('Error:', error)
#             print('Please try again')
#
#
# if __name__ == '__main__':
#     main()

# try:
#     3 / 0
# except:
#     pass
#
# print('Program flows further')

# class MyObject:
#     def __del__(self):
#         print(self, 'is about to be deleted')
#
#
# obj = MyObject()
# del obj
#
# obj = MyObject()
# print(id(obj))

# class ObjectWithDestructor:
#     def __del__(self):
#         print('destructor invoked')
#         raise Exception
#
#
# print('Creating object...')
# obj = ObjectWithDestructor()
#
# print('Deleting reference...')
# del obj
#
# print('Done')

# try:
#     try:
#         raise ValueError
#     except ZeroDivisionError:
#         print('division by zero')
# except AttributeError:
#     print('attribute error')

# def main():
#     try:
#         raise ValueError('value is incorrect')
#     except ValueError as error:
#         print('Exception:', error)
#         raise
#
#
# try:
#     main()
# except ValueError:
#     print('ValueError detected')

# try:
#     raise ValueError
# except ValueError:
#     raise ZeroDivisionError

# a = 5
# b = 0
#
# try:
#     result = a / b
# except ZeroDivisionError as error:
#     raise ValueError('variable b is incorrect')from error

# MAX_STARS = 30
# WIDTH = 80
#
#
# def print_result(number):
#     if number==0:
#         stars_count=MAX_STARS
#     else:
#         stars_count = round(MAX_STARS / number)
#         if stars_count > MAX_STARS:
#             stars_count = MAX_STARS
#
#     number_field_width = WIDTH - 2 * stars_count
#     stars = '*' * stars_count
#     fmt = '{0}{1:^' + str(number_field_width) + '}{0}'
#
#     print(fmt.format(stars, number))
#
#
# def divide_numbers():
#     while True:
#         try:
#             first_number = float(input('First number: '))
#             second_number = float(input('Second number: '))
#             result = first_number / second_number
#         except(ValueError, ZeroDivisionError)as error:
#             print('Error:', error)
#             print('Please try again')
#             print()
#         else:
#             print_result(result)
#             break
#
#
# if __name__ == '__main__':
#     divide_numbers()

# def fn():
#     try:
#         # raise ZeroDivisionError
#         return
#     finally:
#         print('finally block')
#
#
# fn()

# import warnings
#
# name = input('Enter your first and last name: ')
#
# if name.count(' ') != 1:
#     warnings.warn('Name format may be incorrect')
#
# print('Hello, ', name, '!', sep='')
