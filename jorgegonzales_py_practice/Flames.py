# FLAMES Game
#
# Write a program which implements Flames.
#
# Flames is an interesting game that people play to learn about their relationships.
# Flames is named after the acronym: Friends, Lovers, Affection, Marriage, Enemies, and Siblings.
# It is a popular game among young people, especially those beginning to explore the world of crushes.


def name_grinder(name1, name2):
	"""Function to find differences in names' letters"""
	name1 = set([i for i in name1.lower() if i.isalpha()])
	name2 = set([j for j in name2.lower() if j.isalpha()])
	return len(name1.symmetric_difference(name2))  # we get different symbols for set name1 and name2


def flames_game(name1, name2):
	"""The flames game"""
	selector = "FLAMES"[name_grinder(name1, name2) % 7]
	relations = {selector == "F": "Friends",
	             selector == "L": "Lovers",
	             selector == "A": "Affectionate",
	             selector == "M": "Married",
	             selector == "E": "Enemies",
	             selector == "S": "Siblings"}[True]
	return name1 + " and " + name2 + " are " + relations


print("""Welcome to the FLAMES game!
Rules are: you enter two names, you get their relations\n""")

name1 = input("Please enter the first name!\n")
name2 = input("Please enter the second name!\n")
print(flames_game(name1, name2))