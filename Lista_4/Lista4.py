import requests
import json

city = input("Podaj nazwę miasta: ")

forecast = input("Czy chcesz pogodę na dzisiaj czy na jutro? (dzisiaj/jutro): ")

api_key = "3a6d40b17935fe3eb18051086c0f5810"

if forecast == "dzisiaj":
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pl"
elif forecast == "jutro":
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric&lang=pl"

response = requests.get(url)
weather_data = json.loads(response.text)
 
if forecast == "dzisiaj":
    print(f"Aktualna temperatura w {city} to {weather_data['main']['temp']} stopni Celsjusza.")
    print(f"Ciśnienie w {city} to {weather_data['main']['pressure']} hPa.")
    print(f"Wilgotność w {city} to {weather_data['main']['humidity']} %.")
    print(f"Opis pogody: {weather_data['weather'][0]['description']}.")
else:
    print(f"Prognoza pogody na jutro w {city} to {weather_data['list'][1]['weather'][0]['description']}.")
    print(f"Temperatura na jutro w {city} to {weather_data['list'][1]['main']['temp']} stopni Celsjusza.")
    print(f"Ciśnienie na jutro w {city} to {weather_data['list'][1]['main']['pressure']} hPa.")
    print(f"Wilgotność na jutro w {city} to {weather_data['list'][1]['main']['humidity']} %.")
