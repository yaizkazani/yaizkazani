# Seat Reservation
#
# If you've ever been in a concert, you are aware that you buy tickets to be able to reserve a seat inside a stadium.
# The seat you will be on will have a specific number or code that would enable you to know exactly how far or how close you are to the stage.
#
# Note: if you are kind of uncomfortable with lists, here's a reference to get you started.
#
#     Create a simple seat reservation program
#     Create a list that would store dashes '-' as a symbol that the seat is still available to take.
#     Define a function that would loop over the list and print out the seats horizontally or in a 3 x 3 position. Refer to this image for reference.
#     Define a second function that would check if the seats are occupied. This should check if the list contains "X" in each element,
#     which is the symbol that we will use if the seat is taken that you will store in a variable. If the variable is equal to 9 (the total number of seats),
#     return True (and break from the loop), and False if not.
#     Create a loop that would have to (1) ask the user for the number of seat he would want to reserve, (2) print out the chairs,
#     (3) check if all the seats are occupied and (4) ask the user now if he/she wants to reserve again.
import keyboard


def chair_reservation(choice, db):
    """main function"""
    if choice == "1":
        seat_chosen = input("\nPlease enter sit number you'd like to reserve (0 - 9), default is 0\n")
        try:
            seat_chosen = int(seat_chosen)
        except:
            seat_chosen = 0
        if db[seat_chosen // 3][seat_chosen % 3] == "X":  # we convert input N of seat to our db indexes and check if sit is busy
            return "busy_error"
        else:
            db[seat_chosen // 3][seat_chosen % 3] = "X"  # same and reserve the seat
            return "success" + str(seat_chosen)
    elif choice == "2":  # print our database
        for item in db:
            print(*item)
        return free_sit(db)
    elif choice == "3":  # we call for free_sit to check if there are free sits or no
        return free_sit(db)
    elif choice == "4":
        if input("Do you want to reserve another place? Input: Yes / Any to exit").lower() == "yes":
            return chair_reservation("1", db)  # we go to reserve another seat
        else:
            return "exit"


def free_sit(db):
    """check if there are free seats in db"""
    return "Yes" if len([item for sublist in db for item in sublist if item == "_"]) else "No"  # Oookay.. we build a list of items of sublists of db if they're == "_"
                                                                                                # meaning that this sit is free. If there are at least 1 element in this list
                                                                                                # - conditions will work


db = list(["_" for i in range(3)] for x in range(3))  # we fill our database with "_" meaning free sits

while 1:  # main menu loop

    print("""Welcome to seat reservation application!
             Options:
                1 - Reserve a place
                2 - Print reservation status
                3 - Check if there are free seats
                4 - Reserve another seat (actually we don't need this)   
          """)
    choice = input("Please enter your choice!\n")
    result = chair_reservation(choice, db)
    if result == "busy_error":  # we handle result of main functions stored in variable result
        print("Selected seat is busy, try another!")
        continue
    elif "success" in result:
        print("You have successfully reserved a seat! Number is:", result[7:])  # we need to cut stuff a little since we know that it starts
                                                                                # with success and len("success") = 7
    elif result == "exit":
        print("You have decided to exit")
        break
    print("There are free seats") if str(result) == "Yes" else print("No more free seats, sorry !", *chair_reservation("2", db))

