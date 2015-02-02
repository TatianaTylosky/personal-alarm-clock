from time import strftime
from os import system
import sys
import pywapi #weather API
import string #weather API
import requests #so I can get the json file for ip address
import json

def F(X):
	Y = X * 9/5 + 32
	return str(Y)

print """Welcome to Tati's alarm clock!"""

# while True:
#     #input = raw_input("What would you like to do?")
#     time = strftime("%H:%M:%S")
#     print time
#     #print type(time)
#     if time == "22:10:00":
#         print "ring!"
#         system('say "Smashing morning Tatiana"')


print "ring!"



system('say "Good morning Tatiana!....."')

url = "http://ipinfo.io/json"
data = requests.get(url)
print data.json()
your_location = data.json()
zip = your_location['postal']
city = your_location['city']

where = 'say "...based on your I.P. address, you\'re probably in"' + city

system(where)

weather_com_result = pywapi.get_weather_from_weather_com(zip)

temp = weather_com_result['current_conditions']['temperature']
system("say 'Today's weather is." + string.lower(weather_com_result['current_conditions']['text']) + " with a temperature of " + temp + "degrees celcius or " + F(int(temp)) + " degrees Fahrenheit.\n\n'")

int_temp = int(temp)

if int_temp < 0:
	system("say 'You definitely want to wear an extra coat....and scarf and gloves, it's freezing out there'")
elif 0 < int_temp < 5:
	system("say 'It is cold, you are going to want a coat'")
elif 5 < int_temp < 10:
	system("say 'It is reasonably cold, you are going to want an extra sweather'")
elif 10 < int_temp < 15:
	system("say 'You want a sweater, but it is nice out.'")
elif 15 < int_temp < 20:
	system("say 'It should be nice out but you may want a sweater.'")
elif 20 < int_temp < 25:
	system("say 'Gorgeous weather today! You can even wear shorts if you'd like.")
elif 25 < int_temp < 30:
	system("say 'Nice and warm out today! Wear something light.")
elif 30 < int_temp:
	system("say 'It is hot out! Stay cool today.")
else:
	system("say 'Sorry but I am not sure what clothes you should wear today. Something must be wrong with the weather API.'")






