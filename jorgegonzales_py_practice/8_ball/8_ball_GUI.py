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
from tkinter import scrolledtext
from tkinter import messagebox


def ask_clicked():  # clear fields first, call for magic_ball function
    clear_clicked()
    ans.insert(INSERT, magic_ball(txt.get()))


def clear_clicked():
    ans.delete(1.0, END)
    txt.delete(0, END)


def play_clicked():
    clear_clicked()
    messagebox.showinfo("", "Let's play again!")


def quit_clicked():
    window.destroy()


def magic_ball(question):
    print("Thinking.", sep="", end="")
    for x in range(random.randint(1, 3)):  # adding dots to "Thinking" line
        ans.insert(INSERT, ".")
        window.update_idletasks()  # to make dots appear, otherwise they wont properly appear
        time.sleep(1)
    print("")
    with open("8_ball_answers.txt", mode="r", encoding="UTF-8") as ans_file:
        for i in range(random.randint(0, 19)):  # scrolling file for a random answer
            next(ans_file)
        return ans_file.readline()  # return line that will be used as answer


# we create a window here↓
window = Tk()
window.title("Amazing Magic 8 Ball")
window.geometry("900x400")

# we create a header label↓
lbl = Label(window, text="Amazing Magic 8 Ball", font=("Lucida Console", 20))
lbl.grid(column=0, row=0, columnspan=3)  # we allow this to use few columns (as i understand) for beauty

# we create text input field and label for it↓
txt_lbl = Label(window, text="ASK YOUR QUESTION HERE >>>")
txt_lbl.grid(column=0, row=2, sticky="E")
txt = Entry(window, width=27)
txt.grid(column=1, row=2, sticky="W")
txt.focus()  # we make input field to have focus on it after window appears

# we create buttons ↓
ask_btn = Button(window, text="Ask the question", bg="purple", fg="white", command=ask_clicked)
ask_btn.grid(column=0, row=1)
clear_btn = Button(window, text="Clear", bg="purple", fg="white", command=clear_clicked, width=22)
clear_btn.grid(column=1, row=1, sticky="W")
play_again_btn = Button(window, text="Play Again!", bg="purple", fg="white", command=play_clicked)
play_again_btn.grid(column=2, row=1)
quit_btn = Button(window, text="Quit", bg="purple", fg="white", command=quit_clicked)
quit_btn.grid(column=3, row=1)

# we create scrolled_text type answer field↓

ans = scrolledtext.ScrolledText(window, width=20, height=10, font=("Lucida Console", 10))
ans.grid(column=1, row=3)

window.mainloop()  # main function for window - wont work if we doesnt run it !
