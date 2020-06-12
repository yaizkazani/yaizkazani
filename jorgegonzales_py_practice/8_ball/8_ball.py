# Magic 8 Ball
#
#     Simulate a magic 8-ball.
#     Allow the user to enter their question.
#     Display an in progress message(i.e. "thinking").
#     Create 20 responses, and show a random response.
#     Allow the user to ask another question or quit.
#     Bonus:
#         Add a gui.
#         It must have box for users to enter the question.
#         It must have at least 4 buttons:
#             ask
#             clear (the text box)
#             play again
#             quit (this must close the window)

import random, time
from tkinter import *


def magic_ball(question):
    print("Thinking.", sep="", end="")
    for x in range(random.randint(0, 5)):  # adding dots to "Thinking" line
        print(".", sep="", end="")
        time.sleep(1)
    print("")
    with open("8_ball_answers.txt", mode="r") as ans_file:
        for i in range(random.randint(0, 19)):  # scrolling file for a random answer
            next(ans_file)
        return ans_file.readline()  # return answer


print(magic_ball(input("Ask your question ! \n")))  # calling function and getting question
