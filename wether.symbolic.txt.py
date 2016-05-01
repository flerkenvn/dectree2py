#!/usr/bin/python3
def classify(outlook, humidity, windy):
	if outlook == "sunny":
		if humidity == "high":
			return "no"
		if humidity == "normal":
			return "yes"
	if outlook == "overcast":
		return "yes"
	if outlook == "rainy":
		if windy == "TRUE":
			return "no"
		if windy == "FALSE":
			return "yes"
