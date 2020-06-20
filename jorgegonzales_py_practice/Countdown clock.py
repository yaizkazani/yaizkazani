# Countdown Clock
#
#     Create a program that allows the user to choose a time and date, and then prints out a message at given
#     intervals (such as every second) that tells the user how much longer there is until the selected time.
#     Subgoals:
#         If the selected time has already passed, have the program tell the user to start over.
#         If your program asks for the year, month, day, hour, etc. separately, allow the user to be able to type in either the month name or its number.
#         TIP: Making use of built in modules such as time and datetime can change this project from a nightmare into a much simpler task.
# time.mktime(t) - преобразует кортеж или struct_time в число секунд с начала эпохи. Обратна функции time.localtime.
# datetime.timetuple() - возвращает struct_time из datetime.
import time


def transformer(ctime):
    """Function to convert seconds into days/hours/minutes if necessary"""
    if ctime > 86400:
        return ctime // 86400, "days", (ctime % 86400) // 3600, "hours", ((ctime % 86400) % 3600) // 60, "minutes", (((ctime % 86400) % 3600) % 60), "seconds"
    elif 86400 > ctime > 3600:
        return ctime // 3600, "hours", (ctime % 3600) // 60, "minutes", ((ctime % 3600) % 60), "seconds"
    elif 3600 > ctime > 60:
        return ctime // 60, "minutes", (ctime % 60), "seconds"
    else:
        return ctime, "seconds"


def countdown_timer(dt_struct):
    """Function to count remaining time till given date"""
    dt_ctime = time.mktime(dt_struct)  # we convert our structured time into current time in seconds since epoch
    timeleft = dt_ctime - time.time()  # we find remaining time amount in seconds
    if timeleft < 0:
        print("Please try again, the time you've selected is in the past")
    else:
        while 1:  # we run cycle for showing remaining time
            timeleft = int(dt_ctime - time.time())  # we use int to remove fractional part
            print("Time left:", *transformer(timeleft))
            # delta = datetime.timedelta(seconds=timeleft)  # using timedelta to get time left in seconds
            # print(datetime.time.strftime((datetime.datetime.min + delta).time(), "%H:%M:%S")) # first arg is datetime formatted into time, second one is format
            time.sleep(1.0)
            if timeleft <= 0:
                break


while 1:
    dt = input(("""Hello ! Please enter the date and time in following format:
%d %b %Y HH:MM:SS
for example 10 Jun 2020 22:00:00\n"""))
    try:
        dt_struct = time.strptime(dt, "%d %b %Y %H:%M:%S")  # we check if input value has proper format
        break
    except:
        print("Incorrect input, try again!")

countdown_timer(dt_struct)
