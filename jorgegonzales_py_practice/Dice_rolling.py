"""No GUI"""
# Dice Rolling Simulator
#
# By using the random module, Python can do things like pseudo-random number generation.
#
#     Allow the user to input the amount of sides on a dice and how many times it should be rolled.
#     Your program should simulate dice rolls and keep track of how many times each number comes up (this does not have to be displayed).
#     Finally, print out how many times each number came up.
#     Subgoals:
#         Adjust your program so that if the user does not type in a number when they need to, the program will keep prompting them to type in
#         a real number until they do so.
#         Put the program into a loop so that the user can continue to simulate dice rolls without having to restart the entire program.
#         In addition to printing out how many times each side appeared, also print out the percentage it appeared. If you can,
#         round the percentage to 4 digits total OR two decimal places.

from random import randint


def dice_roller(dice):
    """ function to create pseudorandom dice rolls"""
    return randint(1, dice)


count = dict()  # dictionary for counting rolls
while 1:
    while 1:  # looped input prompts
        dice_sides = input("Please enter number of sides the dice should have")
        rolls = input("Please enter number of rolls")
        if not (dice_sides.isdigit() or rolls.isdigit()):  # checking if inputs are correct
            print("Incorrect input, try again")
        else:
            break
    for i in range(int(rolls)):  # how many time to roll
        result = dice_roller(int(dice_sides))
        count[result] = count.get(result, 0) + 1  # count results using dict
    tmp = sorted(list((count.keys())))  # since dicts are unordered we need a list to keep keys sorted
    for key in tmp:
        print("The number:", key, "showed", count[key], "times and it's:", round((count[key] / int(rolls)) * 100, 2), " percents of total rolls")
        # ↑ we go through dict's keys
        # and show the string with required data
