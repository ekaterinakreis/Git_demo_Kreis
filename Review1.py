# list = [1, 2, 3]
# list1 = []
# list2 = list(range(4))
# list = [1, 2, 'as', 'False', [1, 2, 3]]
# list1 = []
# print(len(list))
# print(2 in list)
# if 10 in list:
#     print("Yes!")
# else:
#     print("No!")

# lst = [1, 4, 3, 5, 19, 10, -10]
# lst1 = ["Anna", 'Dima']
# print(sum(lst))
# print(min(lst))
# print(max(lst))

# lst.append(45.0)
# print(lst)
# lst.extend(lst1)
# print(lst)
# del lst[0]
# print(lst)
# lst.clear()
# print(lst)

# a = lst.pop()
# print(a)
# print(lst)

# lst.reverse()
# print(lst)
# lst2 = lst.copy()
# print(lst)
# print(id(lst))
# print(lst2)
# print(id(lst2))

# lst += [100]
# print(lst)

# for i in lst:
#     print(i, end=" ")
# print(lst)
# print(*lst)

# num = [i for i in range(10) if i % 2 !=0]
# print(num)
# ________________________________________________

# num1 = [1, 2, 3]
# num2 = (1, 2, 3)
# num1[1] = 10
# num2[1] = 10
# print(num1)
# print(num2)
#
# print(num1.__sizeof__())
# print(num2.__sizeof__())

# b = list(num2)
# b[1] =15
# c = tuple(b)
# print(c)

# number = (2, 6, 9, 1, 8)
# num1 = sorted(number)
# print(num1)

# _______________________
# num =  {1,2, 3, 4, 5, 5}
# print(set(num))
# print(len(num))
# print(max(num))
# print(min(num))

# for i in num:
#     print(i)
# num1 = {1, 3, 4, 5}
# num2 = {1, 2, 3, 4, 5}
# print(num == num1)
# print(num == num2)

# sorted_num = sorted(num)
# print(sorted_num)

# a = {1, 2, 3}
# c = {5, 6, 7}
# a.remove(6)
# a.discard(6)
# b = a.copy()
# print(b)

# a.add(19)
# print(a)
# a.update(c)
# print(a)

# my_set1 = {1, 2, 3, 4}
# my_set2 = {10, 30, 40}
# a = my_set1.union(my_set2)

# a = my_set1.intersection(my_set2)
# print(a)
# b = my_set1.symmetric_difference(my_set2)
# print(b)
# # c = my_set1.difference(my_set2)
# c = my_set1^my_set2
# print(c)
# d =  my_set1^my_set2

# print(my_set2.issubset(my_set1))
# print(my_set1.issuperset(my_set2))
# print(my_set2.issuperset(my_set1))
# print(my_set1.isdisjoint(my_set2))

# num = {int(i) for i in range(int(input()))}
# print(num)

# ___________________________
# dct = {
#     'USA': '+1',
#     'Rus': '+7',
#     'Turkey': '+30'
# }
# dct = {}
# print(type(dct))
# dct1 = dict(USA = +1, Russia = +7, Turkey = +30)
# dct2 = dict([['USA', 1], ['Russia', 7], ['Turkey', 30]])
# print(dct2)

# dct = {
#     'USA': '+1',
#     'Rus': '+7',
#     'Turkey': '+30'
# }
# if 'FRANCE' in dct:
#     print('YES')
# else:
#     print('NO')
# print(len(dct))

# dct1 = {
#     'name': 'Anna',
#     'age': " "
# }


#  Слияние словарей
# dct3 = dct | dct1
# print(dct3)

# for key in dct.keys():
#     print(key)

# for key in dct:
#     print(key)
#
# for values in dct.values():
#     print(values)

# for values in dct:
#     print(values)
#
# for key, value in dct.items():
#     print(key, value)

# print(*dct, sep='\n')
# print(type(*dct))

# print(dct.get('USA'))
# print(dct1.get('age'))
# print(dct.get('France', 'нет такой страны'))

# print(dct.setdefault('FRANCE', '+3'))
# print(dct)

# print(dct.pop('Turkey'))
# print(dct)

# print(dct.popitem())
# print(dct.popitem())
# print(dct)


# dct = {
#     'USA': '+1',
#     'Rus': '+7',
#     'Turkey': '+30'
# }
# keys = list(dct.keys())
# print(keys)
#
# values = list(dct.values())
# print(values)
#
# items = list(dct.items())
# # items = tuple(dct.items())
# print(items)

