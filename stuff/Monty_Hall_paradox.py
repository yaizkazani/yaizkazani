# Monty Hall problem solution
# doors = {1: "Prize",
#          2: "Goat",
#          3: "Goat"
#          }
import random
number_of_doors = 3


def game(selection, doors):
    switch = False
    opened_door = random.choice([i for i in doors.keys() if doors[i] != "Prize" and i != selection])
    if random.choice([0, 1]) == 1:
        selection = int("".join(random.choice([str(i) for i in doors.keys() if i != selection and i != opened_door])))
        switch = True
    return ("Win", switch) if doors[selection] == "Prize" else ("Lose", switch)


stats = dict()
doors = dict()
for i in range(20000):
    prize_door = random.randint(1, number_of_doors)
    for j in range(1, number_of_doors + 1):
        doors[j] = "Goat" if j != prize_door else "Prize"
    selection = random.randint(1, number_of_doors)
    result = game(selection, doors)
    stats[result] = stats.get(result, 0) + 1

print(f'If you switch the door you win {stats[("Win", True)]} times\nIf you DONT switch you win {stats[("Win", False)]} times')


