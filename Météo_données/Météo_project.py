import requests
def get_weather(city):  
    response = requests.get(f'http://api.weatherstack.com/current?access_key=ma_cléAPI&query={city}')
    return response.json() # Utilisez la fonction pour obtenir la météo pour une ville spécifique 
weather_data = get_weather('Montpellier')
print(weather_data)




import datetime

def get_weather(api_key, location):
    base_url = "http://api.weatherstack.com/current"
    params = {
        "access_key": api_key,
        "query": location
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def display_weather(data):
    current = data['current']
    location = data['location']['name']
    weather_icon = current['weather_icons'][0]
    temperature = current['temperature']
    localtime = data['location']['localtime']
    weather_description = current['weather_descriptions'][0]

    print(f"Location: {location}")
    print(f"Weather Icon URL: {weather_icon}")
    print(f"Temperature: {temperature}°C")
    print(f"Local Time: {localtime}")
    print(f"Weather Description: {weather_description}")

api_key = "ma_clé API"
location = "Montpellier"
data = get_weather(api_key, location)
display_weather(data)


