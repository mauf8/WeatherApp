import requests


api_key = "cfbbc5bef98b2b80e66c72487c234ff9"
# API KEY URL https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=cfbbc5bef98b2b80e66c72487c234ff9


def get_weather_icon(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_list = data.get("weather",[])
        #checks if the weather_list is empty, if its not empty return weather icon
        if weather_list:
            icon = weather_list[0].get("icon","")
            iconUrl = "http://openweathermap.org/img/w/"+icon+".png"
            print(iconUrl)
            return iconUrl

        return None


def get_weather_description(city):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        # if the status code is 200(OK), make the data to json
        data = response.json()
        desc = data['weather'][0]['description']

        usedDescription = f"Weather Description: {desc}"

        return usedDescription


def get_weather_Name(city):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        # if the status code is 200(OK), make the data to json
        data = response.json()
        name = data['name']

        usedName = f"City name: {name}"

        return usedName

def get_weather_Temp(city):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        #if the status code is 200(OK), make the data to json
        data = response.json()
        temp = data['main']['temp']

        #tempture was in kelvin, so i changed it to celsius by - 273.15
        temp = int(temp) - 273.15

        #rounding the number from float-point number to a single digit
        finalTemp = round(temp)

        usedTemp = f'Temperature: {finalTemp} Celsius'

        return usedTemp
