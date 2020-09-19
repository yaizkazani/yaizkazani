# """
# Tuples
# """
#
# mytuple = (1, 2, "a", "what's this", {})
# print(mytuple)
# print(len(mytuple))  # Можно узнать длину кортежа
# """
# Addressing elements by indices
# """
# print(mytuple[0])
# print(mytuple[-2])
# print(mytuple[1:3])  # и тут можно сделать срез
#
# """
# Singleton
# """
# singleton = (1, )
# print("OY im a singleton", singleton)
#
# """
# Evaluation and unpacking
# """
#
# evaluation = (1, 2 + 3, "a", "b", "a" + "b")  # обратите внимание на то что выражения ВСЕГДА вычисляются до ЗНАЧЕНИЯ
# print(evaluation)
#
# unpack_me = ("As you may see", "we can unpack lists or tuples", "into multiple variables, however count must match :)")
# a, b, c = unpack_me
# print(a, b, c)
# #z, x, c, v = unpack_me  # MUST_MUSH_MAH_VALUES_COUNT
#
# """
# Tuples are immutable
# """
#
# immut = (1, 2, 3)
# #immut[2] = "a"
# print("Immutable!", immut)
#
# """
# Looping tuples
# """
#
# for i in range(len(mytuple)):
#     print("mytuple i'th element is: ", mytuple[i])  # Выглядит так себе, верно? Скоро научимся подставлять значение переменных в строки и даже выражений
#
# #=============================================================================
#
# """
# Lists
# """
#
# l = [1, 2, 3, 4, 5]
#
# slice = l[2:4]  # Обратите внимание - правый край отрезка не входит в отличие от левого !
# print("Let's slice our list", slice)
#
# element = l[0]
#
# print("Getting 1st element which has index 0: ", element)
#
# """
# List concatenation and replication
# """
#
# l1 = ["a", "b", "c"]
# l2 = ["d", "e", "f"]
#
# print("Lists support contatenation :", l1 + l2)
# print("Replication is also supported :", l1 * 2)
#
# """
# Looping through list
# """
# l = [1, 2, 3]
# for i in range(len(l)):  # в этом случае мы обращаемся по индексам
#     print(l[i])
#
# for item in l:  # в этом случае мы просто перебираем элементы листа, т.к. лист это iterable
#     print(item)
#
# for letter in "string":  # ОФФТОП: мы также можем перебрать строку - нет проблем
#     print(letter)
#
# """
# Changing elements of the list, creating true copies
# """
# l = [1, 2, 3]
# l[0] = "I was changed!"
# print(l)
# l[0] = 1
#
# for item in l:
#     item += 1
#
# print(l)  # элементы листа не изменились, почему?
#
# for i in range(len(l)):  # да потому что мы их и не изменяли :)
#     l[i] += 1
# print(l)
#
# l_copy = l
# l[0] = "Lets change this element again"
# print(l, l_copy)  # Изменения были внесены в оба листа, как так?
# l[0] = 1
#
# l_true_copy = l[
#               :]  # срезы позволяют создать НОВЫЙ ОБЪЕКТ В ПАМЯТИ, а не только копировать ссылку, есть и другие способы, например модуль copy
# l[0] = "Lets change this element once more"
# print(l, l_true_copy)
#
# """
# Deleting elements, in and not in
# """
#
# l = [1, 2, 3]
# print(l)
# del l[0]
# print(l)
#
# # keyword in позволяет проверить есть ли элемент в итеририуемом типе данных, например:
#
# print(3 in l)
#
# if 3 in l:
#     print("3 is an element of l")
#
# if 2 not in l:
#     print("2 is not an element of l")
#
# """
# Value unpacking with lists, enumerate, *
# """
#
# l = [1, 2, 3]
# a, b, c = l
# print(a, b, c)
#
# print(enumerate(l))  # Чё?
# print(*enumerate(l))  # Так то лучше ! :) Звёздочка распаковывает итерируемый объект !
# print(*[1, 2, 3])  # Распаковали лист
# """
# list(), tuple()
# """
# t = (1, 2, 3)
# print(list(t))
# print(tuple(list(t)))
# #==========================================================
# """
# Import, random
# """
# l = [1, 2, 3]
# import random  # импорт МОДУЛЯ
# from random import shuffle  # импорт ф-ии shuffle
# print(random.choice(l))  # возвращает псевдорандомный элемент iterable
# shuffle(l)  # шафлер, тащемта
# print(l)
# print(random.randint(10, 100))  # возвращает псевдорандомное значение из диапазона
#
# #================================================================
#
# """
# List methods
# """
#
# l = [1, 2, 3, 4, 5, 1]
# print("count, index ")
# print(l.count(1))  # два вхождения
# print(l.index(1))  # первый элемент с индексом 0 был найден, ищется первое вхождение
# print(l.index(1, 1))  # находим второе вхождение элемента, перепрыгнув через первый.
#
# print("append")
# print(l.append(6))  # метод ничего не возвращает!! конструкции вида l = l.append(x) до добра не доведут вас
# print(l)
#
# print("extend")
# l2 = [7, 8, 9]
# print(l.extend(l2))  # ничего не возвращается, список меняется in place
# print(l)
#
# print("remove")
# print(l.remove(1))  # возвращается None !
# print(l)
#
# print("insert")
# print(l.insert(0, "string"))  # возвращается None !
# print(l)
#
# print("reverse")
# print(l.reverse())  # возвращается None !
# print(l)
#
# print("sort, sorted")
# l[9] = 1  # мы не можем сравнить int и str, поэтому нужно привести список к одному типу
# print(l.sort(reverse=True))  # инвертируем нашу сортировку, с помошью ключевого аргумента reverse
# print(l)
#
# print(sorted(l))  # если вам нужно значение - используйте ф-ю sorted() - она вернёт вам значение, в отличие от метода .sort()
#
# print("pop")
# print(l)
# print(l.pop())
# print(l)
# print(l.pop(0))
# print(l)
## =============================================================================================
#
# """
# .split(), "".join()
# """
#
# string = "a b c d e f"
# string2 = "a_b_c_d_e_f"
# list_to_join = [1, 2, 3, 4, 5]
#
# print(string.split())
# print(string2.split())
# print(string2.split("_"))
# print("".join(map(str, list_to_join)))
# print(*map(lambda x: x ** 2, list_to_join))
#
# print(list(map(int, input().split())))
