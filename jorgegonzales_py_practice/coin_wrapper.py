# When some people receive change after shopping, they put it into a container and let it add up over time.
# Once they fill up the container, they'll roll them up in coin wrappers which can then be traded in at a bank for what they are worth.
# While most banks will give away coin wrappers for free, it's convenient to have an idea of how many you will need.
# Instead of counting how many coins you have, it's easier to separate all of your coins,
# weigh them, and then estimate how many of each type you have and then how many wrappers you'll need. For example,
# if you weigh all of your dimes and see that you have 1276.9g of them, you can estimate that you have about 563 dimes (since each one is 2.268g)
# and you would be able to fill 11 dime wrappers.
#
# Here is the weight of each coin and how many fit inside each type of wrapper.
#
#     Allow the user to input the total weight of each type of coin they have (pennies, nickels, dimes, and quarters).
#     Print out how many of each type of coin wrapper they would need, how many coins they have, and the estimated total value of all of their money.
#     Subgoals:
#         Round all numbers printed out to the nearest whole number.
#         Allow the user to select whether they want to submit the weight in either grams or pounds.
import math


def coin_scales(weight, name, db):
    coin_value = db[name][0]
    coin_weight = db[name][1]
    coin_count = weight // coin_weight
    return coin_count, coin_count * coin_value


db = {"cent": (0.01, 2.5, 50), "nickel": (0.05, 5, 40), "dime": (0.1, 2.268, 50), "quarter": (0.25, 5.670, 40),
      "half": (0.5, 11.34, 20),
      "dollar": (1, 8.1, 25)}  # 1- value % of one dollar 2- weight of a single coin 3- number of coins in wrapper
ans = dict()
total_value = 0
while True:
    print("1 - Select coin type \n",
          "2 - Add a new coin \n",
          "3 - Reset total \n",
          "4 - Quit \n", sep="")
    select = input("Please select the option\n")
    if select in ["1", "2", "3", "4"]:
        select = int(select)
        if select == 1:
            while True:
                print(*map(lambda x: str(x[0]) + " " + x[1], list(enumerate(db.keys()))),
                      sep="\n")  # we generate options list based on our database
                select = int(input())
                if len(db) > select > -1:
                    coin_name = list(db.keys())[select]
                    break
                else:
                    print("You have chosen the wrong option, try again!")
            coin_weight = 0
            coin_weight_input = input("Please input selected coin weight\n")
            coin_weight = int(coin_weight_input) if coin_weight_input.isdigit() else print(
                "Coin weight input is not correct, you have entered: ", coin_weight_input)
            coin_number, coins_value = coin_scales(coin_weight, coin_name,
                                                   db)  # we unpack results of coin_scales to variables
            total_value += coins_value
            ans[coin_name] = ans.get(coin_name, [0 for now in
                                                 range(3)])  # adding empty list if we haven't count that coin type yet
                                                             # and adding values if it's not the first time we count it
            ans[coin_name][0] += coin_number
            ans[coin_name][1] += coins_value
            ans[coin_name][2] = math.ceil(ans[coin_name][0] / db[coin_name][2])

            for key in ans.keys():  # we print cumulative result for user's coins
                print("You have ", ans[key][0], " ", key, " s", ", you need ", ans[key][2], " wrappers for them",
                      sep="")
            print("Your coin's total approximate value is: ", round(total_value), "$")
            select = ""

        elif select == 2:
            while True:
                print("You have selected to add a new coin\n",
                      "Please enter coin parameters: name\n"
                      "value( in % to one dollar, ex. 10c will have 0.1)\n"
                      "weight(grams)\n"
                      "number of coins that fit single coin wrapper\n\n",
                      "To continue enter 1\n"
                      "To leave this menu input 0 or exit",
                      sep="")
                select = input()
                if select == "0" or str(select).lower() == "exit":  # user decided not to add coin
                    select = ""
                    break
                if int(select) == 1:  # user decided to continue
                    new_coin_name = str(input("Please enter coin's name  "))
                    new_coin_value = float(input("Please enter value( in % to one dollar, ex. 10c will have 0.1)  "))
                    new_coin_weight = float(input("Please enter weight in grams  "))
                    new_coin_wrapper = int(input("Please enter wrapper capacity  "))
                    if db.get(new_coin_name, 0) == 0:  # we do not have this coin in database
                        db[new_coin_name] = [new_coin_value, new_coin_weight, new_coin_wrapper]
                        print("New coin added, parameters are: ", new_coin_name, ": ", db[new_coin_name])
                        break
                elif not select.isdigit():
                    print("You have entered non digit value(only exit allowed)\nTry again!", sep="")

        elif select == 3:
            print("Total sum was reset!")
            ans = dict()
            total_value = 0
        elif select == 4:
            print("Exiting!")
            break
