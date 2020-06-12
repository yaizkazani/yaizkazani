# Menu Calculator
#
# Imagine you have started up a small restaurant and are trying to make it easier to take and calculate orders. Since your restaurant only sells 9 different items,
# you assign each one to a number, as shown below.
#
#         Chicken Strips: ($3.50
#         French Fries: ($2.50
#         Hamburger: ($4.00
#         Hotdog: ($3.50
#         Large Drink: ($1.75
#         Medium Drink: ($1.50
#         Milk Shake: ($2.25
#         Salad: ($3.75
#         Small Drink: ($1.25
#
# To quickly take orders, your program should allow the user to type in a string of numbers and then it should calculate the cost of the order.
# For example, if one large drink, two small drinks, two hamburgers, one ho:d(og, and a salad are ordered, the user should type in 5993348,
# and the program should say that it costs $19.50. Also, make sure that the program loops so the user can take multiple orders without having
# to restart the program each time.
#
#     Subgoals:
#         If you decide to, print out the items and prices every time before the user types in an order.
#         Once the user has entered an order, print out how many of each item have been ordered, as well as the total price.
#         If an item was not ordered at all, then it should not show up.


db = {  # we create a dictionary that will contain our menu
    1: ("Chicken_Strips", "$3.50"),
    2: ("French Fries", "$2.50"),
    3: ("Hamburger", "$4.00"),
    4: ("Hotdog", "$3.50"),
    5: ("Large Drink", "$1.75"),
    6: ("Medium Drink", "$1.50"),
    7: ("Milk Shake", "$2.25"),
    8: ("Salad", "$3.75"),
    9: ("Small Drink", "$1.25")
}


def receipt_printer(input_string, db):
    """ function to create a dictionary that contains our order"""
    count = dict()  # dict for counting
    order = dict()  # dict containing order
    tmplist = [i for i in str(input_string) if i.isdigit()]  # we split our string to digits, non-digits are ignored
    for tmp in tmplist:
        count[tmp] = count.get(tmp, 0) + 1  # count our order using dictionary
    for key in count.keys():  # we go though count dict and put values into order dict
        price, amount, item = float(str(db[int(key)][1]).replace("$", "")), int(count[key]), db[int(key)][0]  # assigning values
        total = price * amount
        order[item] = amount, total  # put values into order dict
    return order


while 1:
    print("Type Menu for menu, Exit to exit\nInput your order")
    user_input = input()
    if user_input.lower() == "menu":
        print("""
        Chicken Strips: $3.50
        French Fries: $2.50
        Hamburger: $4.00
        Hotdog: $3.50
        Large Drink: $1.75
        Medium Drink: $1.50
        Milk Shake: $2.25
        Salad: $3.75
        Small Drink: $1.25
              """)
        continue
    elif user_input.lower() == "exit":
        break
    myorder = receipt_printer(user_input, db)
    total_price = 0

    for key in myorder.keys():
        print("{:<20}{:^10}{:<10}".format(key, myorder[key][0], myorder[key][1]))
        total_price += myorder[key][1]

    print("{:<10}{:>24}".format("\nTotal:", total_price))
