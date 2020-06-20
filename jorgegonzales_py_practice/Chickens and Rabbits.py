# Chickens and Rabbits
#
# Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among
# the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
#
# Hint: Use for loop to iterate all possible solutions.


def chinese_puzzle(legs=94, heads=35):
	max_rabbits = 94 // 4  # we need to know how many rabbits could be on the farm
	print("Possible solutions found:")
	for rabbits in range(1, max_rabbits + 1):  # we loop through all possible rabbits values
		if (legs % (rabbits * 4)) % 2 == 0:  # and check if legs number could belong to N chicken (i.e. even)
			print("Rabbits:", rabbits, "Chicken:", (legs - (rabbits * 4)) // 2)


chinese_puzzle()