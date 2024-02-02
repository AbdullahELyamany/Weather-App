
import requests

API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # From https://home.openweathermap.org/api_keys
URL = 'https://api.openweathermap.org/data/2.5/weather'


for i in range(5):
    CITY = input("\n\nEnter Your City: ")
    REQ_URL = f"{URL}?q={CITY}&appid={API_KEY}"

    response = requests.get(REQ_URL)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = round(data['main']['temp'] - 273.15, 2)
        print(f"Weather: {weather},  Temperature: {temperature}°C")
    else:
        print("An error occurred")
