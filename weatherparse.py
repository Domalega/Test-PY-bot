from pyowm import OWM
from pyowm.weatherapi25 import forecast
from Sourses import configForWeather, url, alfavit, step
import requests

'''def GetWeatherToday(city):
    weatherToken = configForWeather['API_WEATHER']
    owm = OWM(weatherToken)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    return {
        'city' : city[0].upper() + city[1:],
        'temp' : w.temperature('celsius')['temp'], 
        'clouds' : w.detailed_status,
        'wind' : w.wind()
    }'''

def GetWeather(city = "Novosibirsk", day = "today"):
    if day == 'сегодня':
        day = "today"
    elif day == "завтра":
        day = "tommorow"

    weatherToken = configForWeather['API_WEATHER']
    s_city = city
    try:
        resultforecast = requests.get("http://api.openweathermap.org/data/2.5/forecast",
        params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': weatherToken})
        data = resultforecast.json()
        tempToday =  data['list'][0]['main']['temp']
        tempTommorow = data['list'][3]['main']['temp']
        dateToday = data['list'][0]['dt_txt'][:10]
        dateTommorow = data['list'][4]['dt_txt'][:10]
        if day == "today":
            return {
                'city' : city,
                'date' : dateToday,
                'temp' : tempToday
            }
        elif day == "tommorow":
            return {
                'city' : city,
                'date' : dateTommorow,
                'temp' : tempTommorow
            }
        #dateTommorow1 = data['list'][11]['dt_txt'][:10] +3 первому дню +8 к последующим


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

GetWeather()