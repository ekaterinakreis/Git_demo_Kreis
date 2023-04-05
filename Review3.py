# def func(value):
#
#     def inner(a):
#         return value * a
#
#     return inner
#
# a = func(5)
# print(a(2))
# print(a(6))

# def decor(func):
#
#     def inner(x, y):
#         print("Start")
#         func(x, y)
#         print('Finish')
#
#     return inner
#
# @decor
# def say(name, last_name):
#     print(f"Hello, {name} {last_name}!")
#
# # say = decor(say)
# say('Denis', 'Denisov')


# def func1(func):
#
#     def inner(*args, **kwargs):
#         print("Hi")
#         func(*args, **kwargs)
#         print('Bye')
#
#     return inner
#
# def func2(func):
#
#     def inner(*args, **kwargs):
#         print("Hello")
#         func(*args, **kwargs)
#         print('Goodbye')
#
#     return inner
# @func1
# @func2
# def say(name, last_name):
#     print(f"Hello, {name} {last_name}!")
#
# say('Denis', 'Denisov')

# class Cat:
#     bread = 'Siamese'
#     color = 'black'
#     age = 4

import random
class Ghost(object):
    def __init__(self):
        self.color = random.choice{("white", "yellow", "purple", "red")}
ghost = Ghost()
print(ghost.color)
