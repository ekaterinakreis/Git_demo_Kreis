# def multi(a, b):
#     print(a*b)
#     return a*b
#
# num = (multi(5, 11)) +10
# num1 = multi(10, 11)
# print(num)
# print(num1)

# def say_hello():
#     print('Hello')
# say_hello()

# def check_even(a):
#     if a % 2 ==0:
#         print('Yes')
#     else:
#         print('no')
# for i in range(15):
#     check_even(i)

# def check_even(a):
#     for i in range(a):
#         if a % 2 ==0:
#             print('Yes')
#         else:
#             print('no')
# check_even(10)

# def check_even(a):
#     lst =[]
#     for i in range(a):
#         if a % 2 ==0:
#             lst.append('Yes')
#         else:
#             lst.append('no')
#     return lst
# print(check_even(10))

# def fun():
#     s = 'Hi'
#     print(f'First {s}')
#
# s = 'Hello'
# fun()
# print(s)

#  GLOBAL

# age = 17
#
# def print_age():
#     print(age)
# print_age()

# Local

# def print_age():
#     age = 17
#     print(age)
# print_age()

# def multi():
#     x = 10
#     y = 5
#
#     def sum_fun():
#         c = 20
#         print(x + y + c)
#     sum_fun()
# multi()

# def multi():
#     x = 10
#
#     def sum_fun():
#         c = 20
#         print(x + y + c)
#     sum_fun()
# y = 5
# multi()
#
# def multi(a, b):
#     print(a*b)
# multi(2, 5)

# *a, b, c = [1, 'Hello', 3.5, True]
# print(a, b, c)

a = 5
b = 10
a, b = b, a
print(f'a = {a}')
print(f'b = {b}')