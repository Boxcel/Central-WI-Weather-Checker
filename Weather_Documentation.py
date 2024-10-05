import random
import datetime
import time
import dataclasses

# Weather Documentation
# This is a documentation of the weather conditions and variables that can be used in the weather API
Weather = ['Clear', 'Cloudy', 'Overcast', 'Foggy', 'Rain', 'Snow']
Weather == input("What is your current weather?: ")
if Weather == 'Clear':  
 print("Your current weather is Clear")
elif Weather == 'Cloudy':
  print("Your current weather is Cloudy")
elif Weather == 'Overcast':
    print("Your current weather is Overcast")
elif Weather == 'Foggy':
   print("Your current weather is Foggy")
elif Weather == 'Rain':
   print("Your current weather is Rainy")
elif Weather == 'Snow':
 print("Your current weather is Snowy")
Complex_Weather = ['Wind Chill', 'Ice', 'Sleet', 'Freezing Rain', 'Freezing Drizzle', 'Freezing Fog', 'Blowing Snow', 'Hail',]
Complex_Weather == input("What is the complex weather of your weather?: ")
if Complex_Weather == 'Wind Chill':
  print("Your complex weather is Wind Chill")
elif Complex_Weather == 'Ice':
  print("Your complex weather is Ice")
elif Complex_Weather == 'Sleet':
  print("Your complex weather is Sleet")
elif Complex_Weather == 'Freezing Rain':
  print("Your complex weather is Freezing Rain")
elif Complex_Weather == 'Freezing Drizzle':
  print("Your complex weather is Freezing Drizzle")
elif Complex_Weather == 'Freezing Fog':
  print("Your complex weather is Freezing Fog")
elif Complex_Weather == 'Blowing Snow':
  print("Your complex weather is Blowing Snow")
elif Complex_Weather == 'Hail':
  print("Your complex weather is Hail")
Variables =['Light', 'Moderate', 'Heavy', 'Severe']
Variables == input("What is the severity of your weather?: ")
if Variables == 'Light':
 print("Your weather is Light")
elif Variables == 'Moderate':
  print("Your weather is Moderate")
elif Variables == 'Heavy':
  print("Your weather is Heavy")
Complex_Variables = ['Patchy', 'Intermittent', 'Continuous', 'Occasional', 'Periods of', 'Showers', 'Drizzle', 'Flurries', 'Squalls', 'Thundershowers']
Complex_Variables == input("What is the complex variable of your weather?: ")
if Complex_Variables == 'Patchy':
 print("Your weather is Patchy")
elif Complex_Variables == 'Intermittent':
  print("Your weather is Intermittent")
elif Complex_Variables == 'Continuous':
  print("Your weather is Continuous")
elif Complex_Variables == 'Occasional':
  print("Your weather is Occasional")
elif Complex_Variables == 'Periods of':
  print("Your weather is Periods of")
elif Complex_Variables == 'Showers':
  print("Your weather is Showers")
elif Complex_Variables == 'Drizzle':
  print("Your weather is Drizzle")
elif Complex_Variables == 'Flurries':
  print("Your weather is Flurries")
elif Complex_Variables == 'Squalls':
  print("Your weather is Squalls")
elif Complex_Variables == 'Thundershowers':
  print("Your weather is Thundershowers")
Temperature = ['Cold', 'Cool', 'Warm', 'Hot']
Temperature == input("What is your current temperature?: ")
if Temperature == 'Cold':
 print("Your current temperature is Cold")
elif Temperature == 'Cool':
  print("Your current temperature is Cool")
elif Temperature == 'Warm':
  print("Your current temperature is Warm")
elif Temperature == 'Hot':
  print("Your current temperature is Hot")
Extreme_Weather = ['Tornado', 'Hurricane', 'Blizzard', 'Flood', 'Drought', 'Heatwave', 'Coldwave', 'Thunderstorm', 'Hailstorm', 'Tsunami', "earthquake"]
Extreme_Weather == input("What is the extreme weather of your weather?: ")
if Extreme_Weather == 'Tornado':
 print("Your extreme weather is Tornado")
elif Extreme_Weather == 'Hurricane':
  print("Your extreme weather is Hurricane")
elif Extreme_Weather == 'Blizzard':
  print("Your extreme weather is Blizzard")
elif Extreme_Weather == 'Flood':
  print("Your extreme weather is Flood")
elif Extreme_Weather == 'Drought':
  print("Your extreme weather is Drought")
elif Extreme_Weather == 'Heatwave':
  print("Your extreme weather is Heatwave")
elif Extreme_Weather == 'Coldwave':
  print("Your extreme weather is Coldwave")
elif Extreme_Weather == 'Thunderstorm':
  print("Your extreme weather is Thunderstorm")
elif Extreme_Weather == 'Hailstorm':
  print("Your extreme weather is Hailstorm")
elif Extreme_Weather == 'Tsunami':
  print("Your extreme weather is Tsunami")
elif Extreme_Weather == 'earthquake':
  print("Your extreme weather is earthquake")
