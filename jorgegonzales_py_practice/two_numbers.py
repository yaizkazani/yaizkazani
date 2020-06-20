# Two Numbers
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


def two_numbers(int_list, target):
	int_list = dict(enumerate(list(map(int, int_list))))  # we make an enumerated dictionary since list have problems
	for key1 in int_list.keys():  # we go through our dict
		for key2 in int_list.keys():  # we go through dict again to make us able compare two elements of dict
			if key1 != key2 and int_list[key1] + int_list[key2] == int(target):  # we do not count if we hit same element twice and if condition is met - we just return keys
				return (key1), (key2)


print("Welcome ! This script returns indices of elements which sum equals given target")
inp = input("Please enter number sequence, non digits are ignored\n")
int_list = [i for i in inp if i.isdigit()]
tgt = input("Please enter target (yes, should be digit)\n")
target = tgt if tgt.isdigit() else None
# f = lambda i: int(i) if i and i.isdigit() else None
# target = f(tgt)
if target and int_list:
	print(two_numbers(int_list, target))
else:
	print("Invalid input, exiting")