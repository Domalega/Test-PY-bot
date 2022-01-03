import telebot
from telebot.types import Message
from weatherparse import *
from Sourses import configForBot 


def Main():
    bot = telebot.TeleBot(configForBot['API_BOT'])

    @bot.message_handler(commands=['start'])
    def sendWelcome(message):
        bot.reply_to(message, "Пробный бот")

    @bot.message_handler(commands=['weather'])
    def sendWeather(message):
        bot.reply_to(message, "Введите город в котором хотите узнать погоду")
        @bot.message_handler(func=lambda m: True)
        def GetWeatherBot(message):
            try:
                weatherData = GetWeather(message.text)
                bot.reply_to(message, "City : " + str(weatherData['city']) +'\nTemperature : ' 
                + str(weatherData['temp']) +'\nClouds : '
                + str(weatherData['clouds']) +'\nWind : '
                + str(weatherData['wind']['speed']))
            except:
                bot.reply_to(message, "Ошибка ввода")
    
    bot.infinity_polling()

if __name__ == '__main__': 
    Main()
