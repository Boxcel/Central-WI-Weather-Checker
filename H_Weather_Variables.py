import random
import datetime
import time
import dataclasses

# Weather Documentation
# This is a documentation of the weather conditions and variables that can be used in the weather API

#User Signing data

User = input("What is your user signture?: ")
print(f"Thank you, {User} weather data input will come next.")
print("")
Weather = ['Clear', 'Cloudy', 'Overcast', 'Foggy', 'Rain', 'Snow']
Wind = ['Calm', 'Breeze', 'Gale', 'Storm', 'Hurricane']
Visibility = ['Poor', 'Moderate', 'Good', 'Excellent']
Precipitation = ['None', 'Light', 'Moderate', 'Heavy']
Humidity = ['Dry', 'Comfortable', 'Humid']
Pressure = ['Low', 'Normal', 'High']
Time = ['Morning', 'Afternoon', 'Evening', 'Night']
Season = ['Spring', 'Summer', 'Autumn', 'Winter']
Day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
Month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
Year = ['2025', '2026', '2027', '2028', '2029', '2030']
Complex_Weather = ['Wind Chill', 'Ice', 'Sleet', 'Freezing Rain', 'Freezing Drizzle', 'Freezing Fog', 'Blowing Snow', 'Hail',]
Complex_Variables = ['Patchy', 'Intermittent', 'Continuous', 'Occasional', 'Periods of', 'Showers', 'Drizzle', 'Flurries', 'Squalls', 'Thundershowers']
Temperature = ['Cold', 'Cool', 'Warm', 'Hot']
Extreme_Weather = ['Tornado', 'Hurricane', 'Blizzard', 'Flood', 'Drought', 'Heatwave', 'Coldwave', 'Thunderstorm', 'Hailstorm', 'Tsunami', "earthquake"]
#OCT/2024, All variables have beeen defined and the code is ready for testing

# User general data
print("")
year = input("What year is it?: ")
month = input("What month is it?: ")
day = input("What day is it?: ")
season = input("What season is it?: ")
time_of_day = input("What time of day is it?: ")
print(f"You have entered the following data: Year: {year}, Month: {month}, Day: {day}, Season: {season}, Time of day: {time_of_day}")
#Weather input data.
print("")
print("Weather conditions available:", Weather)
weather = input("What is your weather like?: ")
print("Wind conditions available:", Wind)
wind = input("What is the wind speed like?: ")
print("Temperature conditions available:", Temperature)
temperature = input("What is your current temperature?: ")
print(f"You have entered the following weather data: Weather: {weather}, Wind: {wind}, Temperature: {temperature}")
#Complex weather conditions user data
print("")
print("Complex weather conditions available:", Complex_Weather)
Complex_Weather = input("What is your complex weather condition?: ")
print("What is your Complex Variable:", Complex_Variables)
#Complex weather conditions user data