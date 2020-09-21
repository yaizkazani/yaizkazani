# """
# %, .format(), fstring
# """
# # % formatting
# print("%s is %d years old" % ("Bob", 15))  # %s placeholder for string values, %d - for decimal digit
# print("My name is %s" % "Bob")  # tuples are necessary only when you pass multiple values
# print("Why % formatting is not cool?")
# print("Look %s, how %s %s we need to %s to a string - looks %s" %("here", "many", "values", "pass", "weird"))
# text = 'We gonna pass float number to different placeholder types'
# number = 4.3
# print('%s %s %d %f %g' % (text, number, number, number, number))
# %d will truncate to integer, %s will maintain formatting, %f will print as float and %g is used for generic number
#
# # %.format() method - POWERFUL!
#
# print("{} I NEVER ASKED FOR THIS!! {} {}".format("mystring", "is formatted", "using .format() method"))
# myvar = 3
# print("{:x<20} {:10} {:*>10} ".format("arg1", "arg2", myvar))
# # As you see .format() is WAY more potent than % formatting - it has builtin language that allows you to do weird things with text
#
# # fstring
# def f(val):
#     return val * 10
# value1 = "Abracadabra"
# value2 = 2
# value3 = 3
# value4 = f  # Aww shit you can put functions into variables :P
# # fstring evaluate anything inside of {}, lets take a look:
# print(f"let's calculate something that we put into braces {{}}: {value4(value2)}, value2 = {value2}, value2 + value 3 = {value2 + value3}")
# # fstring can do tricky stuff like this:
# l = ["Bob", 28, "NY"]
# print(f"{l[0]} is {l[1]} years old and live in {l[2]}")
#
# print(f"Passing quotes in fstring is pain! But ill tell you a secret: strings accept both single and double quoutes so use single :) ' like this ' ")
##===========================================================================
# """
# .sort(), sorted(), key=, reverse=
# """
# l = [1, 3, 2, 18]
# l2 = [1, 2, 3 , "abc", 11, 12, "abcd"]
# l.sort()
# print(f"simple sorted l is {l}",
#       f"let's try to do this: {{l.sort()}} {l.sort()}",
#       f"lee's see how sorted() works: {{sorted(l)}}={sorted(l)}",
#       f"using reverse= {sorted(l, reverse=True)}",
#       f"let's make it more fun with key=: {sorted(map(str, l2), key=len)}",  # we need to make items string, since integers doesnt have length
#       sep="\n")  # NB! we use len, not len() since WE_DO_NOT_CALL_IT !!! Also remember how to use multilevel fstrings
# ============================================================================
#
# """
# lambda functions
# """
#
#
# def simple_function(x):
#     return x ** 2
#
#
# l = lambda x: x ** 2  # these 2 functions are equivalent to each other
# l1 = lambda x: x + 1  # NB! the x is not the same x we define on the next line.
# x = 1
# print(l1(1))
#
# # 2 args lambda
# z, y = 3, 4
# f = lambda x, y: x * y  # this function require 2 args to work
# print(f(z, y))  # we define f as lambda function, we call it and pass it 2 arguments
#
# print((lambda x, y: x + y)(z, y))  # IIFE = Immediate Invoked Function Expression - we pass data to function immediately
#
# """
# Passing lambda to key= in .sort()/sorted()
# """
#
# l = [(1, 0), (8, 1), (10, 2), (13, 44), (22, 11)]
# print(sorted(l, key=lambda x: x[1]))  # here we say to lambda: take second element of x and return it, we must ensure that x has this 2nd element ofc :)
#
# l = [1, 2, 3, 4, 5]
# print(sorted(l, key=lambda x: -x))  # in this case we make lambda return negative value of x, this is equivalent to reversed=True actually in our case
#
# def myfunc(x):
#     return str(x) + " - we change our variable in myfunc()"
#
# x = 1
# y = lambda x: myfunc(x * 10)  # this is weird, you'd betted don't do things like this, its just FYI
# print(y(x))

##=================================================================================
#
# """
# Dictionary. {"All hail": "the King"}
# """
#
# t = ((1, 2), (3, 4))
# d = dict(t)  # conversion from tuple
# print(d)
#
# d1 = {"key": "value",
#       1: "value2",
#       "key2": ["value3", "value4"]
#       }
#
# """
# Dict data access and methods
# """
#
# print(f"Dictionary keys {d1.keys()}")
# print(f"Dictionary values {d1.values()}")
# print(f"Dictionaty items {d1.items()}")
#
# #Checking if key/value is in dict
# print(f"we will use 'in' to check that: {'key' in d1.keys()}")
# print(f"same for values : {'value2' in d1.values()}")
# print(f"however it wont find value inside the list : {'value3' in d1.values()}")
# # To find such values we need to loop through the dict:
#
# for key in d1.keys():
#       if "value3" in d1[key]:
#             print(f"value found in {key} value")
#             break
#
# for key, value in d1.items():
#       print(f"key is {key}, value is {value}")
#
# """
# dict.setdefault(), dict.get()
# """
#
# # These are VERY useful methods, you need to master them
#
# d1.setdefault("new_key", "default_value")
# print(d1)  # this method checks if there is a "new_key" key value in d1 dict, creates if and value is set to "default_value"
#             # this is very useful if you want to proactively tackle possible key errors that happen when you call nonexistent key
#
# get_val = d1.get("new_key", "something")  # .get() tries to get value for key "new_key" if it doesnt exist it returns second argument
# print(get_val)
#
# #.get() could be used to count something with dict. Look here:
#
# import random
# count_dict = dict()
# list_to_count = [random.randint(1, 10) for i in range(10)]  # we can generate lists with generator statements, they are useful, we will talk about them a bit later
# print(list_to_count)
#
# # we have a list and a dict - how to count how many elements of each value are in list? Simple:
#
# for item in list_to_count:
#       count_dict[item] = count_dict.get(item, 0) + 1  # So what we do here: we tell dictionary to set value for key where key is current list element
#                                                       # and the value is previous value if it was in dictionary or 0 if we haven't "seen" such element yet
#                                                       # so we increase it by one.
# print(count_dict)
#
# #================================================================================
# """
# reading and writing files
# """
#
# """
# Using open()
# """
# file = open("2.txt", mode="a", encoding="utf8")  # open file in append mode
# mydata = "This string we put into the file"
# file.writelines(mydata + "\n")  # we put our data into file
# file.close()  # now our data is saved in file
#
# # lets read it to ensure that we have our string added
#
# file = open("2.txt", mode="r", encoding="utf8")
# for line in file.readlines():  # file.readline returns list of strings
#      print(line)
#
# # file.read() / file.write() - just treat a file as sequence of symbols
#
# """
# Using with open()
# """
#
# with open("2.txt", mode="r", encoding="utf8") as file:
#     lines = file.readlines()
#     for s in lines:
#         print(s)
# # at this point file is closed automatically
# # NB! the file objects are iterable so we cannot iterate over them more than one time per creation. example:
#     r = file.read()
#     print(f"r is empty because file is already depleted - iteration was already finished to get lines from .readlines(). r = {r}")
