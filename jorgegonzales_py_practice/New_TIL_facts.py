# Watch for new TIL facts
#
# If you finished the previous project which compared the karma of two new comments, hopefully you learned a thing or two about receiving data from Reddit's API.
# Now you're going to take this a step further, and even have the opportunity to make a basic twitter bot.
#
#     Create a program that receives data from the /r/todayilearned subreddit, and looks for new facts that have been posted.
#     Each time the program comes across a new fact, the fact should be printed into the command line. However, phrases like "TIL ",
#     "TIL that", etc should be removed so the only thing that is printed is the fact.
#
# New TIL API data here
#
# There are a couple things to note about this since you'll more than likely be using a loop to check for new posts.
# According to Reddit's API Access Rules Page, the API pages are only updated once every thirty seconds, so you'll have to
# have your code pause for at least thirty seconds before it tries to find more posts. Secondly, if for some reason you decide to try to
# get data sooner than every thirty seconds, make sure to not send more than thirty requests per minute. That is the maximum you are allowed to do.
#
# There is actually a lot you can do once your program starts receiving facts. Instead of simply printing the facts, here are some ideas
# for what you can do with them. If you currently do not feel like you can accomplish these ideas, feel free to come back later when you have more experience.
#
#     Print the link to the source of the fact too.
#     Try to further clean up the fact by adding punctuation to the end if it is missing, capitalize the first word, etc.
#     Write the facts to a separate text file so you end up with a giant compilation of random facts.
#     Create a bot that posts the facts to twitter. This may sound hard, but it's actually pretty simple by using the Python Twitter Tools module and
#     following the guide posted here.
#     Remember, the maximum amount of characters you can use in a tweet is only 140, so you'll have to filter out facts that are longer than that.
#     By now you should be pretty familiar with python, so if you get ideas for improving your program, go for it!
import json, time
import urllib.request, urllib.error


def get_til_update():
	til_json_url = "https://www.reddit.com/r/todayilearned/.json"
	til_raw_json = json.load(urllib.request.urlopen(til_json_url))
	string = str(til_raw_json["data"]["children"][0]["data"]["title"]).replace("TIL that", "").replace("TIL", "").lstrip().capitalize()
	string += "." if not string.endswith(".") else ""
	return string


first = True
til_update = get_til_update()
print(til_update)
with open("TIL_output.txt", mode="a") as file:
	file.writelines(til_update)
while 1:
	time.sleep(45)
	try:
		result = get_til_update()
	except urllib.error.HTTPError:
		print("Too many requests, sleeping")
		time.sleep(30)
	if til_update == result:
		print("no updates")
	else:
		til_update = result
		with open("TIL_output.txt", mode="a") as file:
			for line in file:
				pass
			if str(line) == til_update:
				pass
			else:
				file.writelines(til_update + "\n")
		print(result)
