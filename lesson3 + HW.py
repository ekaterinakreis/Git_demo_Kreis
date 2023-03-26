#  ---------LISTS------------------
# my_list = [1, 'hello', 2.0, True, False]
# sentence = 'Python is awsome'
# print(sentence.split(' '))
#
# print(my_list[0])
# print(my_list[-1])
# print("before: ", my_list)
# my_list[0] = 25
# print("after: ", my_list)
#
# my_list.append(sentence)
# print(my_list)

# my_list.insert(-2, sentence)
# print(len(my_list))
# print(my_list.count(1))
# print(my_list.index(None))
# my_list1 = [1, 2, 3, 4, 5]
# print(sum(my_list1))
# print(min(my_list1))
# print(max(my_list1))

# my_list2 = [1, 2, 3, 4, 5, [1, 2, 3, 4, 5, [1, 2]]]
# # print(my_list2[-1][-1][1])
# my_list2.reverse()
# print(my_list2)

# For loops in lists
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num**2)

# list comprehenshion
# new_l = [i*i for i in numbers if i % 2 == 0]
# print(new_l)

# ----------TUPLES------------------
# my_tuple = 1, 2, 3
# print(type(my_tuple))
# my_tuple1 = (1, 5, True, "Hello", 3.5)

# name = 'Mark',
# print(type(name))

# decomposition
# my_tuple = ('Apple', "Orange", "Cat")
# a, b, c = my_tuple
# print(a)
# print(b)
# print(c)

# letters = list(my_tuple)
# letters[0] = 'pineapple'
# print(letters)

# Getting index of items
# my_tuple = (1, 5, True, None,  "Hello", 3.5)
# print(my_tuple.index(None))
# result = tuple([item for item in my_tuple if isinstance(item, int)])
# print(result)
#
# print(sum(result))
# print(f'Max is:  {sum(result)}')
# print(f'Length of result is:  {len(result)}')
#
# for (index, item) in enumerate(my_tuple):
#     print(index, item)

# while i < len(my_tuple):
#     print(i, my_tuple[i])
#      i += 1

# fruits = ('apple', ["", ], )
# fruits[1][0] = 'cherry'
# print(fruits)

#  swaping variabels
# a = 5
# b = 7
# a, b = b, a
# print(a, b)

#  passing tuples as an argument in function
# def sum_it(*args):
#     total = 0
#     for num in args:
#         total =total +num
#     return total
# print(sum_it(4, 5, 10, 11))

# def sum_it(*args):
#     l = []
#     print(len(args))
#     for i in args:
#         l.append(i*i)
#     return l
# print(sum_it(2, 5, 10, 20, 15))

# ---------DICTIONARY------
# my_dict = {
#     "name": "Anna",
#     "last_name": "Pavlova",
#     "age": 37,
#     "depart": " IT"
# }
# print(my_dict.items())
# print(id(my_dict))

# print(my_dict["name"])
# print(my_dict['name'])
# my_dict["last_name"] = 'Smirnova'
# print(my_dict)
# print(len(my_dict))
# my_dict['salary'] = 50000
# print(my_dict)

# print(my_dict.keys())
# print(my_dict.items())
# print(my_dict.pop('depart'))
# print(my_dict)
#
# keys = ['name', 'age', 'depart']
# values = ['', '', '']
# employes = dict(zip(keys, values))
# print(employes)

# employes1 = dict(name = 'Jhon', last_name = 'Wick', age = 40)
# print(employes1)

# ----------SETS----------

# my_l = [1, 3, 3, 4, 5, 7, 7]
# print(set(my_l))
#
# set1 = {1, 2, 3, 'one', 'ten', 20}
# set2 = {1, 2, 3, 'one', 'ten', 100, 200}
# set3 = {1, 2, 3}
# print(set1.issubset(set2))
# print(set2.issubset(set1))
# print((set1.intersection(set2)))

# print(set2.difference(set1))
# print(set1.difference(set2))
# print(set1.symmetric_difference(set2))
#
# print(set1.remove(1))
# print(set1)
# print(set1.add(4))
# print(set1)
#
# fs = frozenset({1, 2, 3})
# print(fs.remove(1))

# ++++++++++     HOMEWORK     ++++++++++++

# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

# my_list = ["a", "b", [1, 2, 3], "d"]
# for x in my_list[2:3]:
#     print(*x)
# # or
# third_elem = my_list[2]
# print(*third_elem)


# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
#
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
new_list = []
for i in list_1:
    if type(i) == int or type(i) == float:
        new_list.append(i)
print(sum(new_list))
#
# for i in list_1:
#     if type(i) == str and 'a':
#         print('a')
#     else:
#         print("No")

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# for i in list_1:
#     if type(i) == str and 'a':
#         print('a')
#     else:
#         continue
# #
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# print('Original list: ', list_1)
# print('Sum of all numbers: ', sum([x for x in list_1 if type(x) == int ]))
# print('All words with a: ', [y for y in list_1 if type(y) == str and "a" in y])

# 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж

# list_2 = ['cat', 'dog', 'horse', 'cow']
# tuple1 = tuple(list_2)
# print(tuple1)
# print(type(tuple1))


# list_2 = ['cat', 'dog', 'horse', 'cow']
# tuple1 = (*list_2,)
# print(tuple1)
# print(type(tuple1))

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

# fam1 = input("Who is in family_1 : ")
# fam2 = input("Who is in family_2 : ")
# tuple1 = tuple(fam1.split(", "))
# tuple2 = tuple(fam2.split(", "))
# # print(tuple1)
# # print(tuple2)
# if len(tuple1) > len(tuple2):
#     print(tuple1)
# elif len(tuple1) < len(tuple2):
#     print(tuple2)
# else:
#     print("Equal")

'''Wrong Solution'''

# if len(fam1) > len(fam2):
#     print(fam1)
# elif len(fam1) < len(fam2):
#     print(fam2)
# else:
#   print("Equal")


# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan.
#  В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

# film = {'title': 'Titanic',
#         'director': 'Cameron',
#         'year': '1997',
#         'budget': '200 million',
#         'main_actor': 'DiCaprio',
#         'slogan': 'my heart'}
#
# print(*film.keys())
# print(*film.values())
# print(*film.items())


# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# numbers = my_dictionary.values()
# print(sum(numbers))


# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]

# lst = [1, 2, 3, 4, 5, 3, 2, 1]
# print(list(set(lst)))


# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга

# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#
# print(set1.intersection(set2))
# print(set1&set2)
#
# print(set1.symmetric_difference(set2))
# print(set1 ^ set2)

# print(set1.issuperset(set2))
# print(set2.issuperset(set1))
#
# print(set1.issubset(set2))
# print(set2.issubset(set1))

# for i in set1:
#     if i in set2:

