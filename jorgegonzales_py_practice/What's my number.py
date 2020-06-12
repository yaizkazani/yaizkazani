# What's My Number?
#
# Between 1 and 1000, there is only 1 number that meets the following criteria:
#
#     The number has two or more digits.
#     The number is prime.
#     The number does NOT contain a 1 or 7 in it.
#     The sum of all of the digits is less than or equal to 10.
#     The first two digits add up to be odd.
#     The second to last digit is even and greater than 1.
#     The last digit is equal to how many digits are in the number.
#
# To find out if you have the correct number, click here.
import functools
import sympy


def find_my_number(value):  # Please notice - conditions are going in REVERSED order - the first string in function's if - is the last condition from list ↑
    """Function to find a number using given conditions"""
    digilist = [int(i) for i in str(value)]
    if int(str(value)[-1:]) == len(str(value)) \
            and ((int(str(value)[-2:-1]) % 2 == 0) and (int(str(value)[-2:-1]) > 1)) \
            and ((int(str(value)[:1]) + int(str(value)[1:2])) % 2 == 1) and \
            functools.reduce(lambda x, y: x + y, digilist) <= 10 and \
            (1 not in digilist and 7 not in digilist) and \
            sympy.isprime(value) and \
            len(str(value)) >= 2:
        return value
    return None


for now in range(10, 1000):
    if find_my_number(now) is not None:
        print(now)
        break

