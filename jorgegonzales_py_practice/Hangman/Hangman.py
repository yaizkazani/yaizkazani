# Hangman Game
#
#     Create a program that selects a random word and then allows the user to guess it in a game of hangman.
#     Like the real game, there should be blank spots for each letter in the word, and a part of the body should be added each time the user guesses a letter than is not in the answer.
#     You may choose how many wrong turns the user can make until the game ends.
#     Subgoals:
#         If the user loses, print out the word at the end of the game.
#         Create a "give up" option.

import random
from math import ceil


def draw_hangman(fails, tries):
    """Function to draw pseudographic"""
    index = ceil(fails / (tries / 7))  # we try to make pictures change process smooth, however on low numbers its not that good.
    if index == 7 and fails != tries:
        index = 6
    hangman_pics = {1: """







======
                    """,
                    2: """
 
  |
  |
  |
  |
  |
======
                    """,
                    3: """
  +----+
  |
  |
  |
  |
  |
======
                    """,
                    4: """
  +----+
  |    |
  | 
  |
  |
  |
======
                    """,
                    5: """
  +----+
  |    |
  |  (x . x) 
  |
  |
  |
======
                    """,
                    6: """
  +----+
  |    |
  |  (x . x) 
  |    (  )
  |
  |
======
                    """,
                    7: """
  +----+
  |    |
  |  (x . x) 
  |    (  )
  |    I  L
  |
======
                    """}
    return hangman_pics[index]



def hangman_game(answer):
    """Game itself"""
    print("Welcome to the hangman game!\n",
          "The rules are: you have limited number of tries\n",
          "Each turn you can guess the letter or the word\n",
          "If you run out of tries - you lose\n",
          "Type Surrender to surrender and lose the game!")
    while 1:  # we get tries
        tries = input("Please enter number of tries\n")
        try:
            tries = int(tries)  # we need to be sure that tries is valid integer
            break
        except:
            print("You have entered wrong value for tries, should be integer, entered value is:", tries)
    fails = 0
    open_letters = set()
    wrong_letters = set()
    closed_letters = ["_" for x in range(len(answer))]  # we build a list to show for closed letters
    while 1:  # we run the game in the loop
        print("You have ", tries - fails, "tries left")
        print("The word is: ", *closed_letters, "\nOpened letters are: ", *sorted(open_letters), "\nWrong letters are: ", *sorted(wrong_letters))
        user_ans = str(input("Please guess a letter or the word!\n"))
        if len(user_ans) > 1:  # if user tries to guess a word we process it
            if user_ans == str(answer):
                return "user_win"
            else:
                fails += 1
                print(draw_hangman(fails, tries))
        if "".join(closed_letters) == str(answer):  # if we guessed all letters right, then we stop the game - user wins
            return "user_win"
        elif user_ans in answer and len(user_ans) == 1:  # if we guessed letter right, and its a letter, not word - we open it
            open_letters.add(user_ans)
            indices = []
            indices = [i for i, letter in enumerate(answer) if letter == user_ans]  # search for incides of correct letter in answer
            for i in indices:
                closed_letters[i] = user_ans  # "open" a letter(s) in closed_letters list
        else:
            if fails == 7 or user_ans.lower() == "surrender":  # user lose conditions
                return "user_lose"
            if user_ans not in wrong_letters and len(user_ans) == 1:  # wrong letter guessed
                fails += 1
                print(draw_hangman(fails, tries))
                wrong_letters.add(user_ans)


with open("hangman_dict.txt", mode="r") as file:  # we scroll a file to get a random word as answer
    for i in range(random.randint(1, 125)):
        next(file)
    ans = str(file.readline()).lower().rstrip()

play = hangman_game(ans)
if play == "user_win":
    print("Congratulations! You win !")
elif play == "user_lose":
    print("You have lost you loser !")
    print(draw_hangman(7, 7))
