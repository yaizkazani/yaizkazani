# """
# Lesson 3
# """
#
# """
# while
# """
#
# spam = 0
# while spam < 5:  # условие
#     print('Hello, world.')  # тело цикла
#     spam += 1
#
# """
# continue
# """
# i = 0  # объявляем переменную i
# while i < 5:  # условие цикла
#     if i == 3:  # тело цикла, обратите внимание на сдвиг кода!
#         i += 2  # снова сдвиг для if
#         continue
#     print(i)
#     i += 1
#
#
# i = 0
# while i < 100:
#     if i % 2 == 0:  # если i чётное, то возвращаемся к условию
#         i += 1
#         continue
#     print(i)  # таким образом мы выводим на экран только нечётные i
#     i += 1
#
#
# """
# break
# """
#
# i = 0
# while True:
#     print(i)
#     if i > 100000:  # условие выхода из цикла через break
#         break
#     i += 1
#
#
# """
# Password Swordfish
# """
#
#
# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access granted.')
#
#
# """
# Truthy and falsey
# """
#
# name = ''
# while not name:  #  проверка значения name
#     print('Enter your name:')
#     name = input()
# print('How many guests will you have?')
# numOfGuests = int(input())
# if numOfGuests:  #  проверка значения numOfGuests
#     print('Be sure to have enough room for all your guests.')
# print('Done')
#
# ================================================================
# """
# range
# """
#
# for i in range(5):  # [0 - 5)
#     print(i)
#
# for i in range(5, 10):  # [5 - 10)
#     print(i)
#
# for i in range(11, 100, 2):  # [11 - 100) шаг 2
#     print(i)
#
# """
# break and continue + for
# """
# for i in range(10):
#     if i == 5:
#         continue
#     elif i == 8:
#         break
#     print(i)
#
# ==================================================================
#
# """
# strings and cycles
# """
#
# for i in range(5):
#     print("Current i value is: " + str(i))  # преобразование переменной в строку и конкатенация
#
#
# """
# we put a loop inside a loop so you can loop while looping
# """
# j = 0
# while j < 10:
#     i = 0
#     print("we will go into cycle 2 now")
#     while i < 10:
#         print("We are in the second cycle, i = " + str(i))
#         i += 1
#     j += 1
#     print("We are in the first cycle j value is: " + str(j))
#
#
# """
# sys.exit()
# """
#
## import sys
# i = 0
# while 1:
#     if i == 123456:
#         sys.exit("123456!")
#     i += 1
#
# from sys import exit
#
# for i in range(1, 100):
#     if i % 49 == 0:
#         print(i)
#         exit("wow!")
#==============================================================
## Guess the number !
