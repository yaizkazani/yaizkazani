# Change Calculator
#
#     Imagine that your friend is a cashier, but has a hard time counting back change to customers.
#     Create a program that allows him to input a certain amount of change, and then print how how many quarters, dimes, nickels,
#     and pennies are needed to make up the amount needed. Example: if he inputs 1.47, the program will say that he needs 5 quarters,
#     2 dimes, 0 nickels, and 2 pennies.
#     Subgoals:
#         So your friend doesn't have to calculate how much change is needed, allow him to type in the amount of money given to him and the price of the item.
#         The program should then tell him the amount of each coin he needs like usual.
#         To make the program even easier to use, loop the program back to the top so your friend can continue to use the program without having to close
#         and open it every time he needs to count change.


def change_calculator(change, coins, i):
    if i > 0:
        change_calculator(change % coins[i - 1], coins, i - 1)
        return change // coins[i - 1]


# cash_amount = int(float(input("Please enter cash amount  \n")))
# item_price = int(float(input("Please enter item price  \n")))
change = 1.37
change = int(change * 100)
coins = [1, 5, 10, 25, 50]
print(change_calculator(change, coins, 5))

