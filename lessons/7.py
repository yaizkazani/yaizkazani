"""Set"""
#
# set1 = {1, 2, "3", 2, ("ololo", 1)}
# print(set1)
#
# broken_set = {1, 2, ["any changeable data types are not supported"]}
#
# # Set has function with the same name that could be used to create sets from different data types
# from_list = set([1, 2, 3, 4])
# print(from_list)

# Adding elements / reading elements / removing elements / checking if element is a part of set
#s = {1, 2, 3, 4}
# from_list.add("new")
# print(from_list)
# #
# for item in from_list:
#     print(item, end=" ")
# print("")

# # # Removing is tricky, .remove() will raise an error if element was not found
# s = {1, 2, 3, 4}
# # s.remove(4)
# # print(s)
#
# s.discard(4)  # do not raise an error
# # s.remove(4)  # raise an error
# s = {1, 2, 3, 4}
#
# print(s)
# print(s.pop())  # remove 1st element
#
# s.clear()  # removing all elements
# print(s)
#
# """
# Set methods
# """
#
# s1 = {1, 2, 3, 4}
# s2 = {5, 6, 7, 2}
#
# print(s1.intersection(s2))  # intersection  of sets: ∩
# print(s1.union(s2))  # union: ∪
# print(s1.difference(s2))  # difference: s1 - s2
#
# s3 = {1, 2, 3}
# s4 = {2}
# print(s4.issubset(s3))  # s3 ⊂ s4
# print(s3.issuperset(s4))  # s4 ⊂ s3
#
# s3.difference_update(s4)  # remove all elements of s4 from s3
# print(s3)
#
# print(s3.isdisjoint(s4))  # checks if sets intersect or not
#
# print(len(s3))  # number of elements
#
# """Frozenset"""
#
# d = dict()
# dict_key = frozenset([1, 2, 3, "watermelon"])  # frozen sets are unchangable = hashable = could be used as dict keys
# d[dict_key] = "It works"
#
# dict_key_unhashable = set([1, 2, 3])
# d[dict_key_unhashable] = "It wont work"

# """List comprehension - YES this IS a Python, BABY!"""
#
# string = "abcde"
# result = []
# for letter in string:
#     result.append(letter * 2)
# print(result)
#
# # General synthax:
# # [] - brackets for a list
# # [i for i in iterable if condition] - i is an element of iterable iterable var., condition - anything that can return Boolean
#
# print([i * 2 for i in "abcde"])  # we can use variables or raw data as data source for list generation.

# Add condition

# print([i for i in "abcde" if i in "ace"])  # THAT'S IT !!!
#
# # TODO With such a powerful tool we can filter data, transmute data creating new iterable data objects from any iterable data object
#
#
"""List comprehension usage"""

"""Offtopic: all(), any(), zip()"""

# To understand following examples you need to know few Python builtin functions

# all() - accept any number of Boolean values - return True if all are True, otherwise False
# any() - same, but return True if any element is True
# zip() - takes 2 iterables as argument, return zip object made of tuples that made of argument's elements
#
# print(all([True, False, True]))
# print(all([True, True, True]))
# print(any([False, False, True]))
#
# print(list(zip([1, 2, 3, 4], ["a", "b", "c", "d", "e"])))  # NB! iterables are not equal, singleton tuples are NOT returned!!!
#
# # looking for even numbers in list
# l = [1, 2, 3, 4, 5, 6]
# print(sum([1 for i in l if i % 2 == 0]))
#
# # looking for vowels and replacing letters
# s = "aadfdcbvadfseaaea"
# # print("Yes") if any([i in "aeouiy" for i in s]) else print("No")
# st = "".join([i.replace("a", "c") for i in "aadfdcbvadfseaaea"])
# print(st)
#
# # creating a string
# import random
#
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# print("".join([random.choice(alphabet) for _ in range(100)]))
#
# """Legend: we have a word and need to encrypt it by putting all even index symbols in the beginning,
# leaving odd at the end with order intact"""
#
# # odd + even encryption
#
# s = "watermelon"
#
#
# def encrypt(s):
#     """
#     :param s: string to encrypt
#     :type s: str
#     :return: even symbols + odd symbols
#     :rtype: str
#     """
#     even, odd = "", ""
#     for i in range(len(s)):
#         if i % 2 == 0:
#             even += s[i]
#             continue
#         odd += s[i]
#     return even + odd
#
#
# def decrypt(s):
#     """
#     :param s: string to decrypt
#     :type s: str
#     :return: decrypted string
#     :rtype: str
#     """
#     if len(s) == 1: return s
#     even_odd = len(s) // 2 if len(s) % 2 == 0 else (len(s) // 2) + 1
#     return "".join(["".join(tup) for tup in zip(s[:even_odd + 1], s[even_odd:])]) + (s[even_odd - 1: even_odd] if len(s) % 2 != 0 else "")
#
# print(decrypt(encrypt(s)))
#
# multiplication table

# [print(str("{:<3} " * 10).format(*l)) for l in [[i * j for i in range(1, 11)] for j in range(1, 11)]]  # Yes, lists made with list comprehension could be arguments for another list comprehension!!

# Create list of 1 separated by 0, number of separators grow from 0 to 10

# print([l for sublist in [[1] + ([0] * i) for i in range(11)] for l in sublist] + [1])
#
# #  For given list L put a separator between elements, separator length equals difference between elements values
#
# L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
# print([k for sublist in [[L[i]] + ["_" * (L[i + 1] - L[i])] for i in range(len(L)) if i < len(L) - 1] + [L[-1:]] for k in sublist])
#
# """pathlib"""
#
# import pathlib, os
#
# p = r"c:/temp\lvl1/lvl2\lvl3"  # slashes doesnt matter much - pathlib will handle them
#
# # Let's create some dirs and file to play with
#
# # pathlib.Path.mkdir(pathlib.Path(rf"{p}"), exist_ok=True)  # we cannot create multiple folders with this
# os.makedirs(fr"{p}", exist_ok=True)  # however with os.makedirs() we can do that, NB! fr = stands for fstring + raw type string
# with open(fr"{p}\text.txt", mode="a") as f:  # we open our file for writing, mode = append, path = fstring + raw
#     f.write("data")
#                                              # at this point file is closed
# print(pathlib.Path(p))
# print(type(pathlib.Path(p)))
#
# """cwd(), chdir(), home()"""
#
# print(pathlib.Path.cwd())  # getting current directory we're working with
# os.chdir(r"c:\temp")       # we can change it if necessary
# print(pathlib.Path.cwd())
#
# print(pathlib.Path.home())  # home directory
#
# """ Checking stuff about path"""
#
# p = pathlib.Path(p)
# print(p.is_absolute())
# print(p.is_dir())
# print(p.is_file())
# print(p.exists())           # useful ! :)
#
# """Absolute and relative paths"""
#
# import pathlib, os
#
# p2 = r"c:/temp/lvl1/lvl2"
#
# print(pathlib.Path(p2).is_absolute())  # we prefer to work with absolute paths so better to check just in case
#
# p2 = r"lvl1/lvl2"
#
# print(pathlib.Path(p2).is_absolute())  # this path is not absolute
# print(os.path.abspath(p2))
# print(pathlib.Path.exists(pathlib.Path(
#     os.path.abspath(p2))))  # we can try to make it absolute, however it doesnt produce existing path, so..
#
# os.chdir(r"c:/temp/")
# print(pathlib.Path.cwd())   # .. we need to move to correct directory so we could..
# print(os.path.abspath(p2))
# print(pathlib.Path.exists(pathlib.Path(os.path.abspath(
#     p2))))  # .. convert paths to absolute using proper cwd. Its quite simple since OS doesnt know where is the point for relative path to start from in filesystem
#             # also note that os.path.abspath returns string, not a path object so we have to convert it using pathlib.Path()
#
#
# """ Path structure"""
#
# import os, pathlib
#
# p = pathlib.Path(r"C:\temp\lvl1\lvl2\lvl3\text.txt")
#
# # Path is made of: anchor + parent + name
# # name is made of stem + suffix
#
# print(p.anchor)
# print(p.parent)
# print(p.name)
#
# print(p.stem)
# print(p.suffix)
#
# print(p.drive)
#
#
# """Parents"""
#
# # You you have seen p have an attribute called parents:You you have seen p have an attribute called parents:You you have seen p have an attribute called parents:You you have seen p have an attribute called parents:You you have seen p have an attribute called parents:You you have seen p have an attribute called parents:
#
# for parent in p.parents:  # it contain list of all parent folders
#     print(parent)
#
# print(p.parents[0])  # they are accessible with index
# print(p.parents[len(p.parents) - 1])
#
#
# """Joining paths"""
#
# import os, pathlib
#
# p1 = r"C:\temp\lvl1\lvl2\lvl3"
# p2 = r"text.txt"
#
# print(pathlib.Path.joinpath(*map(pathlib.Path, [p1, p2])))  # we use map to convert strings into paths with pathlib.Path
#
# p1 = pathlib.Path(p1)
# p2 = pathlib.Path(p2)
# print(p1 / p2)  # operator / works as Path.joinpath() for paths
#
# """ Walking a tree"""
#
# for folder, subfolder, filenames in os.walk(r"C:\temp\testing"):  # This is tricky - it walks through all subfolders and return 3 values on each step.
#     print(f"""folder is {folder}
# subfolder is {subfolder}
# filenames: {filenames}
#     """)   # You can use any var. names, I use these ↑ cause they're obvious
