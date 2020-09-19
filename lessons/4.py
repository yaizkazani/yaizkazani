# """
# Slices
# """
#
#mystring = "String"
# s_len = len(mystring)
# print("String length is: " + str(s_len))
#
# s1 = mystring[0:10]
# print("s1 is: " + str(s1))
#
# s2 = mystring[2:]
# s3 = mystring[:5]
# print("s2 and s3 are: " + str(s2) + " " + str(s3) + "\n")
#
# s4 = mystring[-4:]
# print("s4 is " + str(s4))
# s5 = mystring[-4: 5]
# print("s5 is " + str(s5) + "\n")
#
# s6 = mystring[::2]
# print("s6 uses step 2 -  " + str(s6))
# s7 = mystring[::-1]
# print("s7 is reverse - " + str(s7))

##=========================================================

# """
# find(), rfind()
# """
#
# print("strings".find("ring"))
#
# s = "strings"
# print(s.find("s"))
# print(s.rfind("s"), "\n\n")  # few spaces to make it more readable
#
# print("Index of \"str\" in \"strings\" using .find() is  " + str(s.find("str")))
# print("Index of \"str\" in \"strings\" using .rfind() is  " + str(s.rfind("str")))
#
# print("Lets reverse \"strings\" and try to find \"t\", the result is: " + str(s[::-1].find("t")))
##================================================================
#
# """
# replace(), count()
# """
#
# s = "1234121a"
# print(s.replace("1", "!", 2))
#
# print(s.count("12"))
# print(s.count("12", 4, 10))
#
# """
# Functions
# """
#
#
# def f():  # define function
#     print("Hello world!")
# f()  # function call
#
#
# def f1(name="Bob"):  # default argument value set to "Bob"
#     print("Hello " + name)
#
#
# f1()
# f1("Jack")
#
#
# def f2(name="Bob", age="18", gender="Attack Helicopter"):
#     print("Hello " + name + " you are " + age + " years " + "your gender is " + gender)
#
#
# f2()  # default values are used
# f2("Alice", "21", "Helisexual")  # we pass args according to sequence
# f2("Rob", gender="Funny guy")  # we pass args by name, regardless of sequence
#
# #========================================================================================
# """
# Returning values from functions
# """
#
# def f3(val):
#     val += 10
#     return val
#
# def f4(val):
#     return val * 10
#
# print("f3 and f4 were passed value of 10, results are:\n" + str(f3(10)) + "\n" + str(f4(10)))
#
# print("Lets pass result of f4 function execution to another function f3:" + str(f3(f4(5))))
#
# """
# None
# """
#
#
# def f5(val):
#     print("\nHey I am f5 !")
#     print(val * 100)
#
# print("f5 was passed value of 100, result is " + str(f5(100)))  # Wait wat?
#
# print(f4(f5(5)))  # whoops !
#
# #====================================================================================
#
# """
# Global and local variables
# """
#
# a = "i am global"
#
# def loc():
#     b = "i am local"
#     print(a)
#     print(b)
#     #a = "you cannot change me"
#
# def loc2():
#     c = "i am local from loc2!"
#     print(a)
#     print(c)
#     print(b)
#
#
# loc()
# loc2()
#
# """
# global
# """
#
# a = "im global"
#
# def glob():
#     global a  # now we say to interpretator: treat a as global variable a, not as local !
#     print(a)
#     a = "I was changed inside of function, wow!"
#
# #glob()
# print(a)
##============================================================================================
#
# print("Hello", "world!")
# print("Hello", "world!", sep="\n")
# print("\n")
# print("Hello", "world!", sep="\t")
# print("Hello", "world!", end="<EOS>")
# print("Where is new line?")
# print("\"")