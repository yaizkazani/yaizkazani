import tkinter
import winsound
from tkinter.ttk import Combobox
import threading


def run_thread():
	"""Function to run another function in separate thread"""
	global seconds  # we need to use global variable to get data for number of seconds
	option = combo.get()  # we get data from combobox
	if option == "25":
		seconds = 1500
	elif option == "15":
		seconds = 900
	global stop
	stop = False  # we make stop False since we need timer to run for now
	start_timer_btn.grab_release()  # we release the button that was pressed to get us here
	threading.Thread(target=countdown()).start()  # we run countdown function in separate thread


def stop_timer():
	"""Function to set global variable that controls the timer"""
	global stop
	stop = True


def countdown():
	"""Function that refresh timer label and decrease number of seconds left"""
	global seconds
	global stop
	if not stop and seconds:  # checking if timer should run now
		seconds -= 1  # reduce number of seconds
		print("minutes", seconds // 60, "seconds", seconds % 60)  # calculate number of minutes left
		timer_label.configure(text=str(seconds // 60) + ":" + str(seconds % 60))  # updating timer label with calculated minutes and seconds
		window.update()  # update window to display change
		window.after(1000, countdown)  # run countdown function each second
	else:
		threading.Thread(target=playsound).start()  # if timer stopped - play sound


def playsound():
	"""Playing the sound"""
	winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

stop = False  # set global variable
window = tkinter.Tk()
window.title("POMODORO Timer")
window.geometry("300x250")

combo = tkinter.ttk.Combobox(window)  # create combobox
combo["values"] = [25, 15]
combo.current(1)

timer_label = tkinter.Label(window, text="00:00")
start_timer_btn = tkinter.Button(window, text="Start timer", bg="green", fg="white", command=run_thread)
stop_timer_btn = tkinter.Button(window, text="Stop timer", bg="red", fg="white", command=stop_timer)

combo.grid(row=1, column=0)
start_timer_btn.grid(row=1, column=1)
stop_timer_btn.grid(row=1, column=2)
timer_label.grid(row=0, column=2, columnspan=3)

window.mainloop()
