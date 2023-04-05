import sys
# compare = 3 != 4
# print(compare)

# x = 3
# print(x > 3 and x > 8)
# print(x > 3 and x < 8)
#
# print(x > 3 or x > 8)
# print(x > 3 or x < 8)
#
# print(x > 3 and not x > 8)
# print(x < 3 and not x < 8)

# if x == 5:
#     print("Five")
# elif x > 5:
#     print("More than five")
# else:
#     print("Less than five")

# age = int(input("please, enter your age: "))
# if age >= 18:
#     print("Welcome!")
# else:
#     print("Go home, baby!")

# try:
#     num1 = int(input("please, enter your num1: "))
#     num2 = int(input("please, enter your num2: "))
# except ValueError:
#     print("You enter not  a number!")
#     sys.exit()
# operator = (input("operator: "))
# if num2 >= 0 and operator == "/":
#     try:
#         result = num1 / num212
#         print(f'result = {result}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
# else:
#     result = num1 * num2
#     print(f'result = {result}')

# num = 0
# i = 0
# while num <= 5:
#     print(num)
#     # num = num + 1
#     num += 1

# message = "Hello"
# i = 1
# while i < 6:
#     print(i, message)
#     if i == 3:
#         break
#     i += 1

# message = "Hello"
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i, message)




# ________________HOMEWORK____________


# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.

# health = int(input(f'Enter value: '))
# if health >= 0:
#     print("Alive!")
# else:
#     print("Dead!")

# def health_value():
#     live = 100
#     while live >= 0:
#         damage = int(input("Please enter damage value: "))
#         if live - damage >= 0:
#             print("Alive")
#             live = live - damage
#             print(live)
#         else:
#             print("Dead")
#             break

# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным.
# Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”

# num = int(input("Enter your number: "))
# if num % 2 == 0:
#     print(" This number is even!")
# else:
#     print("This number is odd!")

# number = int(input('Введите любое число: '))
# if number%2:
#     print('Нечетное')
# else:
#     print('Четное')

# num1 = int(input('Введите любое число: '))
# if num1 // 2 == num1 / 2:
#     print('Четное')
# else:
#     print('Нечетное')

#
# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008)
# и не являются столетиями (500, 600). Однако, если год делится без остатка
# на 400, он также считается високосным (1200, 2000)

# year = int(input("Enter year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("This is leap year!")
# elif year % 400 == 0:
#     print("This is leap year!")
# else:
#     print("This is not leap year")


# year = int(input("Введите год: "))
# if year%4:
#     print("Невисокосный")
# elif year % 100 < 1 and year % 400:
#     print("Невисокосный")
# else:
#     print("Високосный")

# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью input()

# text = input(f' Enter your text: ')
# num = int(input(f' Enter number of reiteration: '))
# for index in range(num):
#     print(index, text)
# # or
# print(text.split(" ") * num)

# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
# производит заданное арифметическое действие и печатает результат
# в формате: {num1} {operator) {num2) = {result}

# try:
#     n1 = int(input("Please, enter first number: "))
#     n2 = int(input("Please, enter second number: "))
#     op = input('Please, enter operator(/, *, +, -, **, %, //):  ')
#     if op not in '/*+-**%//':
#         print("This is wrong operator, try again!")
#     else:
#         if op == '/':
#             result = n1 / n2
#         elif op == '*':
#             result = n1 * n2
#         elif op == '+':
#             result = n1 + n2
#         elif op == '-':
#             result = n1 - n2
#         elif op == '**':
#             result = n1 ** n2
#         elif op == '%':
#             result = n1 % n2
#         elif op == '//':
#             result = n1 // n2
#         print(f"{n1} {op} {n2} = {result}")
# except ValueError:
#     print(f'This is not number, try again!')
# except ZeroDivisionError:
#     print('Dividing by zero!')
#

# num1 = 0
# num2 = 0
# try:
#     num1 = int(input('Enter number1: '))
#     num2 = int(input('Enter number2: '))
# except ValueError:
#     print('Вы ввели не число')
#     sys.exit()
# operator = input('Operator: ')
# if operator not in '+-*/%':
#     print("""Вы ввели не правильный оператор!""")
#     sys.exit()
# if num2 == 0 and operator == '/':
#     try:
#         result = num1 / num2
#         print(f'{num1} {operator} {num2} = {result}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя')
#         sys.exit()
# elif num2 > 0 and operator == '/':
#     result = num1 / num2
#     print(f'{num1} {operator} {num2} = {result}')
# elif operator == '+':
#     result = num1 + num2
#     print(f'{num1} {operator} {num2} = {result}')
# elif operator == '-':
#     result = num1 - num2
#     print(f'{num1} {operator} {num2} = {result}')
# else:
#     result = num1 * num2
#     print(f'{num1} {operator} {num2} = {result}')

# From Denis T.

# name = input('Здравствуйте! Как ваше имя?  ')
# if not name.isalpha():
#     print('Вы ввели не имя!!! Начните заново!!!')
# else:
#     print(f'Добро пожаловать, {name}!')
#     flag = True
#     while flag:
#         try:
#             number1 = int(input(f'{name}, введите первое число: '))
#             number2 = int(input(f'{name}, введите второе число: '))
#             operator = input(f'{name}, введите оператор (/, +, *, -): ')
#             if operator not in '/*-+':
#                 print(f'{name}, Вы ввели неверный оператор')
#             else:
#                 if operator == '/':
#                     result = number1 / number2
#                 elif operator == '+':
#                     result = number1 + number2
#                 elif operator == '-':
#                     result = number1 - number2
#                 elif operator == '*':
#                     result = number1 * number2
#                     print(f"""{number1} {operator} {number2} = {result}""")
#         except ValueError:
#             print(f'{name}, Вы ввели не число, попытайтесь еще раз!')
#         except ZeroDivisionError:
#             print('Атата!!!! На ноль делить нельзя!!!!')
#
#         text = input(f"""{name}, желаете продолжить? Для выхода нажмите 'N' или 'n'. Для продолжения нажмите 'Enter' """)
#         if text == 'n' or text == 'N' or text == 'Т' or text == 'т':
#             flag = False
#     print(f"""До свидания, {name}! Ждём Вас в следующий раз.""")