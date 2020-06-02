# Higher Lower Guessing Game
#
#     Create a simple game where the computer randomly selects a number between 1 and 100 and the user has to guess what the number is.
#     After every guess, the computer should tell the user if the guess is higher or lower than the answer.
#     When the user guesses the correct number, print out a congratulatory message.
#     Subgoals:
#         Add an introductory message that explains to the user how to play your game.
#         In addition to the congratulatory message at the end of the game, also print out how many guesses were taken before the user arrived at the correct answer.
#         At the end of the game, allow the user to decide if they want to play again (without having to restart the program).
from random import randint


def game(guess, answer):
    print("Your guess is lesser than answer !") if guess < answer else print("Your guess is greater than answer !")


print("Welcome to the Higher-Lower game!\nThe rules are: you guess the number and get reply\nif your number is greater or lesser than the answer")
while True:
    ans = randint(1, 100)
    counter = 0
    while True:
        counter += 1
        player_guess = int(input("Please enter your number (1-100)\n"))
        if ans != player_guess:
            game(player_guess, ans)
        else:
            print("Congratulations ! You have won! ", counter, "attemps were made!")
            break
    if input("Do you want to play again ? YES/NO").lower() == "yes":
        print("OK!")
    else:
        break
