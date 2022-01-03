from pyowm import OWM
from Sourses import configForWeather 


def GetWeather(city):
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
  