# Multiplication Table
#
#     Create a program that prints out a multiplication table for the numbers 1 through 9.
#     It should include the numbers 1 through 9 on the top and left axises,
#     and it should be relatively easy to find the product of two numbers. Do not simply write out every line manually (ie print('7 14 21 28 35 49 56 63') ).
#     Subgoals:
#         As your products get larger, your columns will start to get crooked from the number of characters on each line.
#         Clean up your table by evenly spacing columns so it is very easy to find the product of two numbers.
#         Allow the user to choose a number to change the size of the table (so if they type in 12, the table printed out should be a 12x12 multiplication table).


def print_table_row(size):
    mylist = [i for i in range(1, size + 1)]  # we generate header line of numbers
    format_string = ""
    for f in range(size):
        format_string += "{" + str(f) + ":<5" + "}"  # we prepare a string to format our rows so the columns will look nice
    print("    ", format_string.format(*mylist))
    for i in range(1, size + 1):
        stringlist = [m * i for m in range(1, size + 1)]
        print("{0:<2}".format(i), " ", format_string.format(*stringlist))


print_table_row(int(input("Please enter size of the multiplication table\n")))
