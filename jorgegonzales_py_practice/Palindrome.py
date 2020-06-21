# Palidrome
#
#     Palindrome means anything(here numbers) that reads the same backwards as forwards.
#     Write a program to check if a number is a palindrome or not.
#     For example 12321 is a palindrome since it reads the same forward and backwards.


def is_palindrome(string):
	if len(string) % 2 == 0:
		return True if string[:len(string) // 2] == string[:len(string) // 2 - 1:-1] else False
	else:
		return True if string[:len(string) // 2] == string[:len(string) // 2:-1] else False


print(is_palindrome(input("Please enter the string to check")))