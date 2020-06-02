# Mean, Median, and Mode
#
# In a set of numbers, the mean is the average, the mode is the number that occurs the most, and if you rearrange all the numbers numerically,
# the median is the number in the middle.
#
#     Create three functions that allow the user to find the mean, median, and mode of a list of numbers. If you have access or know of functions
#     that already complete these tasks, do not use them.
#     Subgoals
#         In the mean function, give the user a way to select how many decimal places they want the answer to be rounded to.
#         If there is an even number of numbers in the list, return both numbers that could be considered the median.
#         If there are multiple modes, return all of them.

from functools import *
from math import *


def mean(mylist, digits = 10):
    return round(reduce(lambda x, y: x + y, mylist) / len(mylist), digits)


def mode(mylist):
    count = dict()
    ans = []
    for item in mylist:
        count[item] = count.get(item, 0) + 1
    for key in count.keys():
        if count[key] == max(count.values()):
            ans.append(key)
    return ans


def median(mylist):
    half_len = len(mylist) / 2
    if half_len.is_integer():
        half_len = int(half_len)
        return mylist[half_len - 1:half_len + 1]
    else:
        return mylist[floor(half_len)]


mylist = [int(i) for i in input("Please enter set of numbers that will be used to calculate median, mean and mode")]
digits = input("Optional: Please enter number of decimal places to round mean")

print("Median is:  ", median(mylist))
print("Mean is:  ", mean(mylist), "  rounded to 10 digits by default") if digits == "" \
    else print("Mean is:  ", mean(mylist, int(digits)), "  rounded for", digits, "decimal places")
print("Mode value(s) :", mode(mylist))
