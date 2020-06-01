# 99 Bottles
#
#     Create a program that prints out every line to the song "99 bottles of beer on the wall."
#     Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
#     Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
#     Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down and pass it around, 98 bottles of beer on the wall.

import time


def bottle_song(n):


    if n > 2:
        print("There are ", n, " bottles of beer on the wall ", n, " bottles of beer.",
              "\n", "Take one down and pass it around, ", (n - 1), " bottles of beer on the wall.", sep="")
    elif n == 2:
        print("There are ", n, " bottles of beer on the wall ", n, " bottles of beer.", "\n",
              "Take one down and pass it around, ", (n - 1), " bottle of beer on the wall.", sep="")
    elif n == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.", "\n",
              "Take one down and pass it around, no more bottles of beer on the wall.",
              "\n", "\n", "No more bottles of beer on the wall, no more bottles of beer.", sep="")
        time.sleep(1)
        print("Go to the store and buy some more, 99 bottles of beer on the wall.", sep="")
    else:
        return
    bottle_song(n - 1)


bottle_song(99)
