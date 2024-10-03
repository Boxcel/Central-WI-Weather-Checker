import requests

Weather = ['Clear', 'Cloudy', 'foggy', 'Raniny', 'thunder', 'Snowy', 'Windy']
def get_weather(api_key, location):
    location = 'Eau Claire'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        return weather_description
    else:
        return "Error fetching weather data"

api_key = 'your_api_key_here'
location = 'your_location_here'
current_weather = get_weather(api_key, location)
print(f"The current weather in {location} is: {current_weather}")