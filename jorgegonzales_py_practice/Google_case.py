# GoogleCase
#
#     Its a game which allows you to play with english sentences.
#     User will enter a sentence in any format.(uppercase or lowercase or a mix of both)
#     Program must convert the given sentence in google case .What is a google case style of sentence?[know_about_it_here:]
#     ( It is a style of writing where we replace all lower case letters into upper case letters leaving the initial of all the words).
#     Subgoals:
#         Program must then convert the given sentence in camel case.To know more about camel case click_here
#         Sentence can be entered with any number of spaces.
#
# Hint: If you are dealing with languages such as c then consider the sentences as the char array.


def google_case(sentence):
	"""Function to transform sentence to gOOOGLE cASE"""
	result = []  # we will accumulate words here
	f = lambda w: w[:1].lower() + w[1:].upper() if w else ""  # we make 1st symbol lower and all other upper, also if w (input to lambda) is Null we return ""
	for word in sentence.split():  # we make a list from sentence (we expect it to be with spaces) and go word by word
		result.append(f(word))  # we send words to f function and append returned data to result list
	return result


def camel_case(sentence):
	"""Function to transform sentence to CamelCaseStyle"""
	result = []
	f = lambda w: w[:1].upper() + w[1:].lower() if w else ""  # same as gOOGLE but reversed
	for word in sentence.split():  # same as  gOOGLE
		result.append(f(word))
	result = "".join(result)  # difference here is that we need to put all words together
	return result


print("Hello! this script allows you to make your sentence camel case of google case.\n")
sentence = input("Please enter your sentence!\n")
option = input("Please input 1 for gOOGLE cASE or 2 for CamelCase\n")

while 1:
	if option == "1":
		print(*google_case(sentence))
		break
	elif option == "2":
		print(camel_case(sentence))
		break
	else:
		print("Invalid option, please try again")
