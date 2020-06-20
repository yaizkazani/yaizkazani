# What's the Weather?
#
# If you would like to know the basics of what an API is, check out this post by iamapizza.
#
#     Create a program that pulls data from OpenWeatherMap.org and prints out information about the current weather,
#     such as the high, the low, and the amount of rain for wherever you live.
#     Subgoals:
#         Print out data for the next 5-7 days so you have a 5 day/week long forecast.
#         Print the data to another file that you can open up and view at, instead of viewing the information in the command line.
#         If you know html, write a file that you can print information to so that your project is more interesting. Here is an example of the results from what
#         I threw together.[3]
#     Tips:
#         APIs that are in Json are essentially lists and dictionaries. Remember that to reference something in a list, you must refer to it by what number element
#         it is in the list, and to reference a key in a dictionary, you must refer to it by it's name.
#         Don't like Celsius? Add &units=imperial to the end of the URL of the API to receive your data in Fahrenheit.
# https://openweathermap.org/api
# city ID = 551487
#
# appid = 3b26705731dfea89d73765c2673e591b
#
# http://api.openweathermap.org/data/2.5/weather?id=551487&appid=3b26705731dfea89d73765c2673e591b&units=metric
#
# http://api.openweathermap.org/data/2.5/forecast?id=551487&appid=3b26705731dfea89d73765c2673e591b&units=metric

import json, urllib.request, time


def wind_direction(deg):
	direction = {0 <= deg < 20: "N",
	             20 <= deg <= 30: "N/NE",
	             30 < deg <= 50: "NE",
	             50 < deg <= 70: "E/NE",
	             70 < deg <= 100: "E",
	             100 < deg <= 120: "E/SE",
	             120 < deg <= 140: "SE",
	             140 < deg <= 160: "S/SE",
	             160 < deg <= 190: "S",
	             190 < deg <= 210: "S/SW",
	             210 < deg <= 230: "SW",
	             230 < deg <= 250: "W/SW",
	             250 < deg <= 280: "W",
	             280 < deg <= 300: "W/NW",
	             300 < deg <= 320: "NW",
	             320 < deg <= 340: "N/NW",
	             340 < deg <= 360: "N"}[True]
	return direction


def get_weather(option="today"):
	cityid = "551487"
	appid = "3b26705731dfea89d73765c2673e591b"
	if str(option) == "today":
		request_string = "http://api.openweathermap.org/data/2.5/weather?" + "id=" + cityid + "&appid=" + appid + "&units=metric"
		json_data = json.load(urllib.request.urlopen(request_string))
		str1 = "Current weather at: " + str(json_data["name"]) + " is: " + str(json_data["weather"][0]["description"])
		str2 = "Temperature is: " + str(json_data["main"]["temp"]) + " it feels like " + str(
			json_data["main"]["feels_like"])
		str3 = "Pressure is: " + str(json_data["main"]["pressure"]) + " humidity: " + str(json_data["main"]["humidity"])
		str4 = "Wind is: " + str(json_data["wind"]["speed"]) + " wind direction: " + str(
			wind_direction(int(json_data["wind"]["deg"])))
		try:
			str_rain = "For the last hour there were a " + str(json_data["rain"]["1h"]) + " mm of rain"
		except KeyError:
			str_rain = ""
		str5 = "Cloudiness is: " + str(json_data["clouds"]["all"]) + "%" + str_rain
		str6 = "Calculation time: " + time.ctime(json_data["dt"])
		print(str1, str2, str3, str4, str5, str6, sep="\n")
		with open("Weather_for_today.txt", mode="w") as file:
			file.writelines([str1, "\n", str2, "\n", str3, "\n", str4, "\n", str5, "\n", str6])

	if str(option) == "forecast":
		while 1:
			days = input("Please enter number of days to forecast\n")
			try:
				days = int(days)
				if days <= 40:
					break
				else:
					print("Incorrect input, max it 40 days")
			except:
				print("Incorrect input")

		request_string = "http://api.openweathermap.org/data/2.5/forecast?" + "id=" + cityid + "&appid=" + appid + "&units=metric"
		json_data = json.load(urllib.request.urlopen(request_string))
		print("Forecast for:", days, "days")
		for day in [json_data["list"][i] for i in range(days)]:
			str1 = "Current weather at: " + str(json_data["city"]["name"]) + " is: " + str(day["weather"][0]["description"])
			str2 = "Temperature is: " + str(day["main"]["temp"]) + " it feels like " + str(day["main"]["feels_like"])
			str3 = "Pressure is: " + str(day["main"]["pressure"]) + " humidity: " + str(day["main"]["humidity"])
			str4 = "Wind is: " + str(day["wind"]["speed"]) + " wind direction: " + str(wind_direction(int(day["wind"]["deg"])))
			try:
				str_rain = "For the last hour there were a " + str(day["rain"]["3h"]) + " mm of rain"
			except KeyError:
				str_rain = ""
			str5 = "Cloudiness is: " + str(day["clouds"]["all"]) + "%" + str_rain
			str6 = "Calculation time: " + time.ctime(day["dt"]) + "\n\n"
			print(str1, str2, str3, str4, str5, str6, sep="\n")
			with open("Weather_forecast" + str(days) + ".txt", mode="a", encoding="UTF-8") as file:
				file.writelines([str1, "\n", str2, "\n", str3, "\n", str4, "\n", str5, "\n", str6])


get_weather(input("Hello ! Please type forecast to get forecast or Enter to get weather for today\n"))
