# Random Wikipedia Article
#
# If you've been to Wikipedia, you may have noticed that there is a link to a random article on the left side of the screen.
# While it can be fun to see what article you get taken to, sometimes it would be nice to see the name of the article so you can skip it if it sounds boring.
# Luckily, Wikipedia has an API that allows us to do so Click here. However, there is a dilemma. Since Wikipedia has articles about topics from all over the world,
# some of them have special characters in the title. For example, the article about the spanish painter Erasto Cortés Juárez has é and á in it. If you look at this specific
# article's API, you will see that the title is "Erasto Cort\u00e9s Ju\u00e1rez" and that the \u00e9 and \u00e1 are replacing the two previously mentioned letters.
# (For information about what this is, start by checking out the first half of this page in the documentation).
# To make your program work, you're going to have to handle this problem somehow.
#
#     Create a program that pulls titles from the official Wikipedia API and then asks the user one by one if he or she would like to read about that article.
#     Example:
#         If the first title is Reddit, then the program should ask something along the lines of "Would you like to read about Reddit?" If the user says yes,
#         then the program should open up the article for the user to read.
#         HINT: Click here to see how the article's ID can be used to access the actual article.
#     Subgoals:
#         As mentioned before, do something about the possibility of unicode appearing in the title.
#         Whether you want your program to simply filter out these articles or you want to actually turn the codes into readable characters, that's up to you.
#         Make the program pause once the user has selected an article to read, and allow him or her to continue browsing different article titles once finished reading.
#         Allow the user to simply press ENTER to be asked about a new article.

import urllib.request, urllib.error, json, webbrowser, time


def wiki_random_article():
	url = "https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json"
	try:
		data = json.load(urllib.request.urlopen(url))
	except urllib.error.URLError:
		data = None
		print("Unable to get data")
	if data:
		articles = {}
		for now in data["query"]["random"]:
			articles[now["id"]] = now["title"]
		return articles


print("""Welcome to wiki random article reader !
The rules:
You will be asked if you like to read an article with give description
Type Yes to read it or Enter to skip to the next random article
Type Exit to exit""")

while 1:
	myarticles = wiki_random_article()
	for key in myarticles.keys():
		print("Would you like to read about:", myarticles[key], "?")
		user_input = input().lower()
		if user_input == "yes":
			webbrowser.open("https://en.wikipedia.org/wiki?curid=" + str(key))
			print("Sleeping for 60 seconds")
			time.sleep(60)
		elif user_input == "":
			pass
		elif user_input == "exit":
			print("Exiting\n")
			break
		else:
			print("Wrong input")
