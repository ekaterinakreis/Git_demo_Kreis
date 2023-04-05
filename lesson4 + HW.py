# def calc(a, b):
#     return  a*b
# # print(calc(5, 5))
#
# result = calc(b = 5, a = 3)
# print(result)

# def calc(a, b):
#     print(a*b)
#     return a+b
# # print(calc(5, 5))
#
# result = calc(b = 5, a = 3)
# print(f'Result: {result}')

# def calc(a, b = 5):
#     return  a*b
# print(calc(5))

# def calc(a, b):
#     return  a*b
# print(calc(b = 1, a = 5))

# def person(age, name, last_name):
#     return f'Hello, ny name is {name} {last_name}. I am {age} years old)'
# print(person(20, 'Anna', 'Volk'))

# _________Встроенные функции ___________
# print(sum([5, 6, 7, 4]))
# print(min([5, 6, 7, 4]))

# def pattern(length, char1, char2):
# def pattern(length, char2, char1 = '*'):
#     return (char1 + char2) * length + char1
# print(pattern(8, '*', '-'))

# def pattern(length = 8, char2 = '-', char1 = "*" ):
#     return (char1 + char2) * length + char1
# print(pattern( char2 = '/', length = 8, char1 = "*" ))

# ________LAMBDA___________
# mult = lambda x, y: x*y
# print(mult(5, 6))

l = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5 ]
# filtered = list(filter(lambda x: isinstance(x, int) and x % 2 == 0, l))
#  print(*filtered)
# filtered1 = list(filter(lambda x: isinstance(x, int) or isinstance(x, float), l))
# print(*filtered1)

#
# filtered2 = list(filter(lambda x: not isinstance(x, str), l))
# print(*filtered2)

# l1 = [20, 15, 8, 7, 6]
# l2 = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5 ]


# power = list(map(lambda x: x **2 , l1))
# power = list(map(lambda x: x ** 2 if isinstance(x, int) else x, l))
# print(power)
# print(power)

# ______Moduls_________
# from functools import reduce
#
# result = reduce(lambda x, y: x * y, l1)
# print(result)

# ________Decorators_____
# def my_decorator(func):
#     def wrapper(arg):
#         print('Im a wrapper!')
#         func(arg)
#         print("Finish")
#     return wrapper

# def say_hello():
#     print(f'Hello')
# say_hello = my_decorator(say_hello)
# say_hello()

# @my_decorator
# def say_hello(name):
#     print(f'Hello, {name}')
# say_hello('Stan')

# def milk(func):
#     def wrapper():
#         print('hot milk')
#         func()
#         print("Finish")
#     return wrapper
#
# def sugar(func):
#     def wrapper():
#         print('Add sugar')
#         func()
#         print("Stop")
#     return wrapper
# @sugar
#
# def coffee():
#     print('Coffee')
# coffee()

import time
# print(time.time())

# import datetime
# print(datetime.date.today())
# bdate = 1989
# current_date = datetime.date.today()
# age = current_date.year - bdate
# print(age)
# current_month = current_date.month
# print(current_month)

# import math as m
# print(m.prod(l1))
# import module
# from module import hello, sum
# from module import hello as h
# print(h('Sam'))
# print(sum(5, 4))

# ______NAMESPACE_________
# print(dir(__builtins__))
# print(globals())
# print(f'Locals: {locals()}')
# pattern(8, char2 = '/')
# print(pattern_1)

# var = 'global'
# def func1():
#     def local():
#         print(var)
#     local()
# func1()

# var = 'global'
# def func1():
#     var = 'enclosed'
#     def local():
#         var = "local"
#         print(var)
#     local()
# func1()
# print(f'outside: {var}')

# ______SCOPE________

# import time
# print(time.perf_counter())
#
# def counter()

# __________ HOMEWORK ____________

# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.

# def square(a):
#     return a * 4, a ** 2, round((2 ** 0.5) * a, 2)
#     return f' Perimetr is: {a * 4}', f'Area is: {a**2}', f'Diagonal is: {(2**0.5)*a}'
#
# print(square(5))
# # print(type(square(5)))

# import math as m
# def square(a):
#     return a * 4, a**2, round(m.sqrt(2*(a**2)), 2)
# print(square(5))

# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

# '''Position arg'''
#
# def person(name, last_name, age, position):
#     return f'Hello! My name is: {name}.'"\n" f'My last name is: {last_name}.'"\n" f'I am {age} years old.'"\n" f'My position is: {position}.'
# print(person('John','Smith','35','web developer' ))
#
# '''Any arg'''
#
# def person(**data):
#    print("Data type of argument: ", type(data))
#
   # for key, value in data.items():
#       print('{}: {}'.format(key,value))

    # for key in data:
    #     print(f'{key}')
#
# person(name = 'Jhon', last_name = 'Smith', age = 35, position = ' web developer')
# person(Firstname="John", Lastname="Wood", Country="Wakanda", Age=25, Phone=9876543210)


# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21]
# создайте новый список, содержащий только положительные числа

# my_list = [20, -3, 15, 2, -1, -21]
# positive = list(filter(lambda x: x > 0 , my_list))
# print(sorted(positive))

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
#
# from functools import reduce
#
# my_list = [20, -3, 15, 2, -1, -21]
# multi =reduce(lambda x, y: x * y, my_list)
# print(multi)

# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра

import time


# def decor(func):
#     def counter(*args, **kwargs):
#         start= time.time()
#         print('The Countdown has started!')
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print('Stop the Countdown!')
#         print(f'The Function {func.__name__} works {end_time - start: 2f} sec')
#         return result
#     return counter()
#
# @decor
# def func_a():
#     time.
#     return ('This is Function!')


# print(mathimatic(3, 5, 7))
# print(time.perf_counter())

# import time
#
#
# def time_it(func):
#    def wrapper(*args, **kwargs):
#        start = time.time()
#        result = func(*args, **kwargs)
#        end = time.time()
#        print(f"""Time taken by {func.__name__}: {end - start:.2f} seconds""")
#        return result
#    return wrapper
#
#
# @time_it
# def time_func():
#     print ("""TIME""")
# time_func()



# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
#
import my_calc

# res = my_calc.sum_it(5, 9)
# print(res)
#
# res1 = my_calc.pow_it(2, 5)
# print(res1)
#
# res2 = my_calc.prod(5, 10)
# print(res2)
#
# res3 = my_calc.div_it(5, 0)
# print(res3)

age = int(input('Введите ваш возраст: '))

if age < 7:
    print('Приходите когда-нибудь потом')
if age >= 7 and age <= 18:
    message = input("Не желаете ли сфотографироваться за 3$? да/нет:  ")
    if message == "да":
        price =+3
        print(f"К оплате {price + 10} долларов")
    else:
        print(f"К оплате 20 долларов")
elif age > 18:
    message = input("Не желаете ли сфотографироваться? да/нет:  ")
    if message == "да":
        price =+3
        print(f"К оплате {price + 20} долларов!")
    else:
        print(f"К оплате 10 долларов!")


age = int(input('Введите ваш возраст: '))
# def describe_age(a):
#     return f"You\'re a(n) {a<7 and'Приходите потом'or a<18 and ''or a<65and'adult'or'elderly'}"