from pyowm.weatherapi25 import weather
import telebot
from telebot import types
from telebot.types import Message
from weatherparse import *
from Sourses import configForBot, url, alfavit, step


def Main():
    bot = telebot.TeleBot(configForBot['API_BOT'])

    @bot.message_handler(commands=['start'])
    def sendWelcome(message):
        menuInlineStart = types.InlineKeyboardMarkup()
        #menuReply = types.ReplyKeyboardMarkup()
        #weatherButtonReply = types.KeyboardButton(text = "Узнать погоду")
        #helpButtonReply =types.KeyboardButton(text = "Помощь")
        #menuReply.add(weatherButtonReply, helpButtonReply)
        weatherButtonInline = types.InlineKeyboardButton(text = "Узнать погоду", callback_data = "weatherChoice")
        helpButtonInline = types.InlineKeyboardButton(text = "Помощь", callback_data = "helpChoice")
        menuInlineStart.add(weatherButtonInline, helpButtonInline)
        bot.send_message(message.chat.id, "Старт работы бота", reply_markup = menuInlineStart)


    @bot.message_handler(commands=['help'])
    def sendHelp(message):
        bot.send_message(message.chat.id, "пока что без помощи")

    @bot.message_handler(commands=['weather'])
    def WeatherButtons(message):
        menuInlineWeather = types.InlineKeyboardMarkup()
        todayButtonInline = types.InlineKeyboardButton(text = "сегодня", callback_data = "todayChoice")
        tommorowButtonInline = types.InlineKeyboardButton(text = "завтра", callback_data = "tommorowChoice")
        menuInlineWeather.add(todayButtonInline, tommorowButtonInline)
        bot.send_message(message.chat.id, "Выберите на когда хотите узнать прогноз", reply_markup = menuInlineWeather)

    @bot.message_handler(commands=['getWeather'])
    def sendWeather(message, temp):
        bot.send_message(message.chat.id, "Введите город в котором хотите узнать погоду")
        @bot.message_handler(func = lambda m: True)
        def GetWeatherBot(message):
            if temp == 1:
                try:
                    weatherData = GetWeatherToday(message.text)
                    bot.send_message(message.chat.id, "City : " + str(weatherData['city']) +'\nTemperature : ' 
                    + str(weatherData['temp']) +'\nClouds : '
                    + str(weatherData['clouds']) +'\nWind : '
                    + str(weatherData['wind']['speed']))
                except:
                    bot.send_message(message.chat.id, "Ошибка ввода")
            elif temp == 2:
                try:
                    bot.send_message(message.chat.id, "Еще не сделанно") 
                except:
                    bot.send_message(message.chat.id, "Ошибка ввода\ Еще не сделанно")  

    @bot.message_handler(commands=['import_github'])
    def secret(message):
        data = Secert()
        bot.send_message(message.chat.id, data)

    @bot.callback_query_handler(func = lambda call: True)
    def callbacks(call):
        if call.data == "weatherChoice":
            WeatherButtons(call.message)
        elif call.data == "helpChoice":
            sendHelp(call.message)
        elif call.data == "todayChoice":
            sendWeather(call.message, 1)
        elif call.data == "tommorowChoice":
            sendWeather(call.message, 2)

    bot.infinity_polling()


if __name__ == '__main__': 
    Main()
