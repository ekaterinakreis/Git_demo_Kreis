# s = 'hello world'
# print(s.replace(' ', ''))

# print(s.count('o'))

# w = 'Денисов Денис Денисович'
# w1 = '1, 2, 3, 4, 5'
# print(w.split())
# print(w.split('е'))
# print(w1.split(','))
# w2 = w1.split(',')
# print(''.join(w1))

# w3 = '  123hello123  '
# print(w3)
# # print(w3.strip())
# print(w3.strip().strip('123'))

# w4 = 'hello world'
# # print(w4.find('e', 2, 5))
# print(w4.index('e', 2, 5))

# w5 = 'naMe? WorLd1 TiTle'
# print(w5.upper())
# print(w5.lower())
# print(w5.title())
# print(w5.capitalize())
# print(w5.swapcase())

# w6 = 'qwerty'
# w7 = 'Qwerty'
# w8 = '1234qwe'
# print(w6.islower())
# print(w7.islower())
# print(w8.islower())

# w6 = 'QWERTY'
# w7 = 'QWERTy'
# w8 = '1234Q'
# print(w6.isupper())
# print(w7.isupper())
# print(w8.isupper())

# w6 = '01234'
# w7 = '1,2'
# w8 = '1234Q'
# print(w6.isdigit())
# print(w7.isdigit())
# print(w8.isdigit())
#
# w6 = '01234'
# w7 = 'qwertY'
# w8 = '1234Q'
# print(w6.isalpha())
# print(w7.isalpha())
# print(w8.isalpha())

# a = int(input('Enter a number: '))
# if a % 2 == 0:
#     if a % 10 == 0:
#         print(f'{a} divide by 2 and by 10')
#     else:
#         print(f'{a} divide by 2, but not 10')
# else:
#     print(f'{a} does not divide by 2')

# q = int(input('Enter your score: '))
# if q >= 100:
#     print('5')
# elif q >= 75:
#     print("4")
# elif q >= 50:
#     print('3')
# else:
#     print("2")

# number = int(input("Enter a number"))
# if number < 10:
#     print("1-digital number")
# elif 10<=number<=99
#     print("2-digital number")
# elif 100<=number<=999
#     print("3-digital number")
# else:
#     print('don`t recognize the number')

# x,y = 45,50
# s = x if x >y else y
# print(s)

# value = 5
# match value:
#     case 1:
#         print(1)
#     case 2:
#         print(2)
#     case 3:
#         print(3)
#     case 4:
#         print(4)
#     case 5:
#         print(5)
#     case _:
#         print("did not find")


# c = 0
# while c < 5:
#     print('Hello')
#     c +=1

# c = 0
# while c < 5:
#     if c % 2 == 0:
#         print("Even")
#     else:
#         print('Odd')
#     c += 1

# text = int(input('Enter num: '))
# count = 0
# while text != "stop":
#     num = int(text)
#     count += num
#     text = input("For continue enter number, for finish enter stop")
# print(f"Sum of words is {count}")

# num = 10
# for i in range(1, num+1, 2):
#     print(i)
#
# string_1 = "he3llo1"
# # for i in range(len(string_1)):
# #     print(string_1[i])
#
# for i in range(len(string_1)):
#     if string_1[i].isdigit():
#         print(i, string_1[i])

# print(string_1[0])
