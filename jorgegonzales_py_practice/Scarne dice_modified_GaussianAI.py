# Scarne's Dice
#
# Turn-based dice game where players score points by rolling a die and then: if they roll a 1, score no points and lose their turn, if they roll a 2 to 6:
# add the rolled value to their points choose to either reroll or keep their score and end their turn.
# The winner is the first player that reaches (or exceeds) 100 points.
import random, math
import sys, time


def dice_roll():
	"""Return roll value != 1"""
	roll = random.choice(range(1, 7))
	return None if roll == 1 else roll


def gaussian():
	"""Uses a Box-Muller Transform to sample the standard normal using two random numbers uniformly distributed on [0,1]"""
	u = random.random()
	v = random.random()
	r = (-2 * math.log(u)) ** (.2)  # we changed ** (.5) to **(.2) to reduce reroll chances on higher numbers
	r *= math.cos(2 * math.pi * v) + 2.5
	return r


def modified_gaussian():
	"""Keep sampling and filtering data"""
	while True:
		r = gaussian()
		if 5 >= r >= 3:  # we need only 3 - 5 digits since 2 is always reroll and 6 is not an option for reroll
			return round(r)


def ai_roll(player_roll):
	"""Ai decides to reroll"""
	if player_roll == 1:
		return None
	else:
		ai_choice = modified_gaussian()  # so we have a gaussian number for the roll which appear probability become more likely the lesser roll is
		return "reroll" if ai_choice == player_roll or player_roll == 2 else None  # so we always reroll 2 and 3 will have higher chance to reroll than 4 and than 5


def dice_game(players):
	"""Main function"""
	global ai_mode  # we check if ai mode is enabled
	scores = {}  # we keep scores here
	while 1:  # loops each turn
		for i in range(1, players + 1):  # each player has its own turn
			print("\nPlayer", i, "turn!")
			print("Player", i, "score:", scores.get(i, 0))
			player_roll = dice_roll()  # we get roll value
			if player_roll:
				print("Player", i, "rolled", player_roll)
				if ai_mode:  # this needed to slow the game so ai moves wont be too fast
					time.sleep(1)
			else:
				print("Player", i, "rolled 1 - No points!")
				break
			if ai_mode and i == 2:  # if we play with AI and its AI turn (i == 2)
				choice = ai_roll(player_roll)
			else:
				choice = input("\nIf you want to reroll - type anything, if you accept - press Enter\n")
			if choice:
				player_roll = dice_roll()  # we reroll
				if player_roll:
					print("Player", i, "rerolled", player_roll)
					scores[i] = scores.get(i, 0) + player_roll  # saving scores if we roll > 1
					if ai_mode:
						time.sleep(1)
					if scores[i] >= 100:  # win condition
						print("Player", i, "won !!!")
						sys.exit("Game finished!")  # we exit the game
					break
				else:
					print("Player", i, "rerolled 1 - No points!")
					break
			else:
				scores[i] = scores.get(i, 0) + player_roll  # we do not reroll
				print("Player", i, "score:", scores[i])
				if scores[i] >= 100:
					print("Player", i, "won !!!")
					sys.exit("Game finished!")
				break


print("""Welcome to dice game!
The rules are simple: each turn you roll a dice
If you roll 1 - you lose your turn and get no points
If you roll 2-6 you can choose either to reroll or to keep
If you keep or reroll to more than 1 your score increases by that number
First player to reach 100 points win the game!\n\n""")

ai_mode = input("""Do you want to play vs AI?
Any input to add AI
Enter or empty input to cancel\n""")
ai_mode = "AI" if ai_mode else None

if not ai_mode:
	print("Player mode selected !")
	while 1:  # processing input data used to determine game conditions
		players = input("Please enter number of players\n")
		players = int(players) if players.isdigit() else None
		if players:
			dice_game(players)
		else:
			print("Invalid input")
else:
	dice_game(2)
