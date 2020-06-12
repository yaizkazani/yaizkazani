# Factors of a Number
#
#     Define a function that creates a list of all the numbers that are factors of the user's number.
#     For example, if the function is called factor, factor(36) should return [1, 2, 3, 4, 6, 9, 12, 18, 36].
#     The numbers in your list should be sorted from least to greatest, and 1 and the original number should be included.
#     Remember to consider negative numbers as well as 0.
#     Bonus:
#         Have the program print the factors of the users number in a comma separated string, without a comma after the last number,
#         and without the brackets of a Python list.
#         If the user's number is prime, note it.


def factors(val):
    if int(val) <= 0:
        return 0
    return sorted([i for i in range(1, val + 1) if val % i == 0])  # sorted list of values in range of 1, val + 1 (right border is not counted in Py) if it is a factor of value


print(factors(int(input("Please enter your number\n"))))
