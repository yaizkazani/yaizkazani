# Compare Recent reddit Karma
#
# Since we're all redditors here, let's make something dealing with reddit. If you go to a user's profile and add .json to the end of it,
# you can get the all sorts of Json data about the user (think of Json as a giant dictionary of smaller dictionaries and lists).
# For example, if I go to my own profile and view it's Json data, it would look like this[1].
# At first it might look intimidating, but if you break it down, you can see it's just one giant dictionary with all sorts of information about my latest posts.
#
#     Create a program that gets information about two different users, and then sees whose most recent post received the most karma.
#     The program should then print out which user received more karma, and what the difference was.
#     This is a pretty open project, so I encourage you to take it further by adding more features if you find it interesting.
#     Remember - Elements in a list are referenced by their index numbers while entries in a dictionary are referenced by their keys.
#     Subgoals:
#         Allow the user to put in the name of two different users when the program first begins.
#         If one of the names of the users does not exist (because of a spelling error), print out a message saying so.
#         Allow the user to keep comparing other users until the program is closed.
#         Display the amount of upvotes and downvotes each user received for their posts.
#         Not sure how to turn json data into usable python data? Check this out.

import json
import urllib.request, urllib.error


while 1:
	print("Welcome! This application compare two user's last posts Reddit karma\n")
	user1, user2 = input("Please enter 1st username\n"), input("Please enter 2nd username\n")
	json_url1 = str("https://www.reddit.com/user/" + user1 + ".json")
	json_url2 = str("https://www.reddit.com/user/" + user2 + ".json")

	while 1:
		try:
			opened_url1 = urllib.request.urlopen(json_url1)

		except urllib.error.HTTPError:
			print("Incorrect username1")
			opened_url1 = None

		try:
			opened_url2 = urllib.request.urlopen(json_url2)

		except urllib.error.HTTPError:
			print("Incorrect username2")
			opened_url2 = None

		if opened_url1 and opened_url2:
			break

	data1 = json.load(opened_url1)
	data2 = json.load(opened_url2)
	recent_post_ups1 = data1["data"]["children"][0]["data"]["ups"]
	recent_post_downs1 = data1["data"]["children"][0]["data"]["downs"]

	recent_post_ups2 = data2["data"]["children"][0]["data"]["ups"]
	recent_post_downs2 = data2["data"]["children"][0]["data"]["downs"]

	delta = (recent_post_ups1 - recent_post_downs1) - (recent_post_ups2 - recent_post_downs2)
	delta = -delta if delta < 0 else delta

	print("Difference is", delta, "\nFirst user has:", recent_post_ups1, "ups", recent_post_downs1, "downs", "\nSecond user has:", recent_post_ups2, "ups", recent_post_downs2, "downs")

	exit = input("Type exit to exit or anything to continue\n")
	if exit.lower() == "exit":
		break
	else:
		print("You have chosen to continue\n")
