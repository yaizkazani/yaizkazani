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

while 1:
    def change_calculator(change, coins):
        """ return how many coins of each type needed to give change"""
        ans = []
        for coin in coins:  # we go through coins and check how many times coin with highest value could be taken from change, then we move to lesser coin
            ans.append([change // coin, coin])
            change = change % coin
        return ans


    cash_amount = float(input("Please enter cash amount  \n"))
    item_price = float(input("Please enter item price  \n"))
    change = cash_amount - item_price  # we calculate change amount
    db = {"0.01": "pence",  # dictionary to keep coins names and values
          "0.05": "nickel",
          "0.1": "dime",
          "0.25": "quarter",
          "0.5": "half"
          }
    coins = sorted(list(map(float, db.keys())), reverse=True)  # we make list of coins to pass into function, dict is unordered so need sorted list, order is vital.
    result = change_calculator(change, coins)
    for item in result:
        print("You need: ", int(item[0]), db[str(item[1])] if int(item[0]) < 2 else str(db[str(item[1])] + "s"))  # print result and add "s" to make it right if number > 1


