# Base Jumper
#
#     Create a program that converts an integer to the specified base.
#     The program should ask for 3 inputs. The number to convert. The base the number is in. And the base to convert the number to.
#     The program should accept a base that is in the range of 2 to 16 inclusive.
#     Display the result to the user and ask if they want to exit or convert another number.
#     Subgoals:
#         Do not display leading zero's in the result.
#         Validate that the number entered is valid for the specified base


def base_check(val, base):  # this might not be working, im not 100% sure yet
    symbols = "0123456789abcdefghijklmnopqrstuvwxyz"
    for digit in str(val):
        if digit not in symbols[0: base] or (str(val)[0] == "0" and base != 2):  #we look if digit is in allowed symbols range and we fail all numbers starting with 0 if they're not binary
            return False
    return True


def base_converter(val, base, new_base):
    val = int(str(val), base)
    symbols = "0123456789abcdefghijklmnopqrstuvwxyz"  #list of all possible symbols used as digits
    new_val = ""
    while True:
        rem = val % new_base  # we get least digit
        new_val += symbols[rem]  # add it to result
        val = val // new_base  # reduce value by base
        if val < new_base:  # if value is lesser than base = value is the greatest digit
            new_val += str(val)
            return new_val


while 1:
    while 1:
        val = input("Please enter the value to convert\n")
        base = int(input("Please enter the base it have ([2 - 16] are allowed values)\n"))
        new_base = int(input("Please enter desired base for conversion\n"))
        if base not in range(2, 17) or new_base not in range(2, 17):
            print("Wrong base parameter, please try again")
        elif not base_check(val, base):
            print("Number you have entered to not belong to entered base")
        else:
            print("Base input is correct")
            break

    print(base_converter(val, base, new_base)[::-1])
    if str(input("Do you want to convert another number? Yes/No\n")).lower() == "Yes":
        print("OK")
    else:
        break
