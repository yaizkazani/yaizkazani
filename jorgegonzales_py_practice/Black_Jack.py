# A Variation of 21
#
# If you do not know how 21 (AKA Blackjack) is played, reading the first couple of paragraphs of this wikipedia article may be beneficial.
#
# In this project, you will make a game similar to Blackjack. In this version:
#
#     There is only one player.
#     There are two types of scores: the game score and the round score.
#     The game score will begin at 100, and the game will last for five rounds.
#     At the beginning of the round, the player is given two random cards from a deck and they will be added together to make the player's round score.
#     From here, the player has two options - draw another card to try to get their round score closer to 21, or they can end the round.
#     The player can draw as many cards as they want until they end the round or their round score exceeds 21.
#     At the end of the round, the difference between 21 and the round score is subtracted from the game score, and then the next round begins.
#     After the five rounds, the player is given their total score and the game is over. ---Other Information About The Game---
#     Aces are only worth 1.
#     If a player busts, 21 is subtracted from their total score.
#     All face cards are worth 10.
#     So the point of your program is to allow the user to play the game described above.
#     Subgoals:
#         At the beginning of each round, print the round number (1 to 5).
#         Since this is a text base game, tell the user what is happening. For example, tell him/her when he/she draws a card, the name of the card, when they bust, etc.
#         Create a ranking system at the end of the game and tell the user their rank. For example, if the player finishes with 50-59 points they get an F,
#         60-69 is a D, 70-79 is a C, 80-89 is a B, and 90-100 is an A.
#         At the end of each round, print out the user's total score.
#         This may be the hardest part of the project, depending on how you wrote it. Make sure the deck has 4 of each type of card,
#         and then remove cards as they are drawn. At the end of each round, make the deck have all of the cards again.
import random


def deck_generator():
	"""Function used to generate 52 card deck. Dictionary of enumerated card and card value tuple is returned"""
	names = ["Ace of ", "King of ", "Queen of ", "Jack of ", "10 of ", "9 of ", "8 of ", "7 of ", "6 of ", "5 of ", "4 of ", "3 of ", "2 of "]
	colors = ["Clubs", "Spades", "Diamonds", "Hearts"]
	cards = enumerate([i + j for i in names for j in colors])  # we use generator to make cards from names,colors lists and then enumerate it
	deck = {}
	for card in cards:  # we add cards from cards list into deck dictionary
		if card[1].split()[0] in ["King", "Queen", "Jack"]:  # we check card name to determine its value
			deck[card[0]] = (card[1], 10)
		elif card[1].split()[0] in ["10", "9", "8", "7", "6", "5", "4", "3", "2"]:
			deck[card[0]] = (card[1], int(card[1].split()[0]))  # we know that value equal to card number so we use it to find value
		elif card[1].split()[0] in "Ace":
			deck[card[0]] = (card[1], 1)
	return deck


def draw_a_card(deck):  # use randint to draw a card from the deck
	"""Function to draw random card from the deck"""
	tmp = random.randint(0, len(deck) - 1)
	while 1:  # this needed to avoid index errors that occur when we hit same key twice.
		try:
			card = deck.pop(tmp)
			break
		except:
			tmp = random.randint(0, len(deck) - 1)  # So we draw until we hit another key
	return card


def cards_value(hand):
	"""Function to calculate cards value in hand"""
	total = 0
	for card in hand:
		total += card[1]
	return total


def score_tab(total_score):
	"""Function to calculate final score grade"""
	ranking_table = {100 >= total_score >= 90: "You graded A - wonderful skill !!!",  # we use dictionary here to get proper grade for total_score value
	                 89 >= total_score >= 80: "You graded B - very nice !!",
	                 79 >= total_score >= 70: "You graded C - good job!",
	                 69 >= total_score >= 60: "You graded D - you can do better!",
	                 59 >= total_score >= 50: "You graded F - loser !!!"}[True]
	return ranking_table


def black_jack():
	"""Main function - Black Jack game"""
	print("""Welcome to Black Jack game !!!
	
	The RULES are:

	1. The GOAL: get as much points as possible, but not more than 21 !
	2. The CARD VALUE: Aces - 1 point,
				Face cards - 10 points,
				Number cards - their number
	3. If you bust (get more than 21 point in total in your hand) - you lose the round !
	4. There are 5 rounds in the game, total score will be displayed after.
	""")
	total_score = 100
	for game_rounds in range(1, 6):  # we play 5 rounds
		deck = deck_generator()  # we create a new deck for each round
		hand = []
		round_score = 0
		print("{0:<7}{1:^13}".format("Round:", game_rounds))
		while 1:  # loop for a single round
			print("""\nThe Black Jack menu:
			1 - Draw a card
			2 - Total value of your cards
			3 - Stop the round
			4 - Show your total score""")
			while 1:  # we process players input, NB! we do not check if its int.
				option = input("\nPlease choose an option\n")
				if int(option) in [1, 2, 3, 4]:
					break
				else:
					print("You have entered wrong value, try again")
			if int(option) == 1:
				card = draw_a_card(deck)  # we get a card from the deck
				hand.append(card)  # add it to our hand
				print("\nYou draw", card[0], "!\n")  # print it
				print("Your hand is:")  # print hand
				for c in hand:
					print(c[0])
			elif int(option) == 2:  # get hand's value
				print("\nYour cards has total value of: ", cards_value(hand))
			elif int(option) == 3:  # stop the round. calculate hand value and round score
				round_score = 21 - cards_value(hand)
				print("Round", game_rounds, "is over !! Your hand value is: ", cards_value(hand), "round score is: ", round_score)
				break
			elif int(option) == 4: # show total score
				print("Your total score is:", total_score)
			if cards_value(hand) > 21:  # busted condition
				print("\nYou busted !!! You have", cards_value(hand), "points in your hand")
				round_score = 21
				break
		total_score -= round_score
	return total_score


print(score_tab(black_jack()))
