# Pythagorean Triples Checker
#
#     If you do not know how basic right triangles work, or what a Pythagorean Triple is read these articles on Wikipedia¹ ².
#     Allows the user to input the sides of any triangle in any order.
#     Return whether the triangle is a Pythagorean Triple or not.
#     Loop the program so the user can use it more than once without having to restart the program.


def value_check(val):  # checking if input value is a digit, also we determine if quite signal was sent to us
    if str(val).lower() == "exit" or str(a).lower() == "quit":
        return "quit"
    elif not val.isdigit():
        print("\"", val, "\"", " is not a number", "\n", "Exiting", sep="")
        return str(val + " is not a digit")
    else:
        return val


while True:  # looping welcome message + program
    print("Welcome ! Please enter 3 sides of the triange",
          "application will return \"Yes\" if its Pythagorean Triple", "Type Exit or Quit to exit", sep="\n")
    a = input("Please enter 1st side")
    result = value_check(a)
    if result == "quit" or "is not a digit" in result:
        break
    else:
        a = int(result)
    b = input("Please enter 2nd side")
    result = value_check(b)
    if result == "quit" or "is not a digit" in result:
        break
    else:
        b = int(result)
    c = input("Please enter 3rd side")
    result = value_check(c)
    if result == "quit" or "is not a digit" in result:
        break
    else:
        c = int(result)
    mylist = sorted([a, b, c])  # we have to have c as maximum element here ↓ so we sort sides
    print("YES") if mylist[2] ** 2 == (mylist[1] ** 2) + (mylist[0] ** 2) else print("NO")
