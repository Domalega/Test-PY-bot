from pyowm import OWM
from pyowm.weatherapi25 import forecast
from Sourses import configForWeather, url, alfavit, step
import requests

def GetWeatherToday(city):
    weatherToken = configForWeather['API_WEATHER']
    owm = OWM(weatherToken)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    return {
        'city' : city[0].upper() + city[1:],
        'temp' : w.temperature('celsius')['temp'], 
        'clouds' : w.detailed_status,
        'wind' : w.wind(),
    }

def GetWeatherTommorow(city = "Moscow"):
    weatherToken = configForWeather['API_WEATHER']
    s_city = city
    city_id = 0
    try:
        result = requests.get("https://api.openweathermap.org/data/2.5/find?",
        params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': weatherToken})
        resforecast = requests.get("http://api.openweathermap.org/data/2.5/forecast",
        params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': weatherToken})
        data = result.json()
        #dataForecast = result.
        cities = ["{} ({})".format(d['name'], d['sys']['country']) for d in data['list']]
        city_id = data['list'][0]['id']
        temp = data['list'][0]['main']['temp']
        print('city:', cities)
        print('id:', city_id)
        print('temp:', temp)
        #for i in data['list']:
            #print( i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'] )
        print(resforecast.url)
    except:
        pass


def Secert(message = url):
    res = ''
    for i in message.upper():
        mesto = alfavit.find(i)
        new_mesto = mesto + step
        if i in alfavit:
            res += alfavit[new_mesto] 
        else:
            res += i
    return res.lower()

GetWeatherTommorow()