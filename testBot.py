from pyowm.weatherapi25 import weather
import telebot
from telebot import types
from telebot.types import Message
from weatherparse import *
from Sourses import configForBot 


def Main():
    bot = telebot.TeleBot(configForBot['API_BOT'])

    @bot.message_handler(commands=['start'])
    def sendWelcome(message):
        menuInline = types.InlineKeyboardMarkup()
        menuReply = types.ReplyKeyboardMarkup()
        #weatherButtonReply = types.KeyboardButton(text = "Узнать погоду")
        #helpButtonReply =types.KeyboardButton(text = "Помощь")
        #menuReply.add(weatherButtonReply, helpButtonReply)
        weatherButtonInline = types.InlineKeyboardButton(text = "Узнать погоду", callback_data = "weatherChoice")
        helpButtonInline = types.InlineKeyboardButton(text = "Помощь", callback_data = "helpChoice")
        menuInline.add(weatherButtonInline, helpButtonInline)
        bot.send_message(message.chat.id, "Кнопка с выбором", reply_markup = menuInline)
        
    @bot.message_handler(commands=['help'])
    def sendHelp(message):
        bot.send_message(message.chat.id, "пока что без помощи")

    @bot.message_handler(commands=['weather'])
    def sendWeather(message):
        bot.send_message(message.chat.id, "Введите город в котором хотите узнать погоду")
        @bot.message_handler(func = lambda m: True)
        def GetWeatherBot(message):
            try:
                weatherData = GetWeather(message.text)
                bot.send_message(message.chat.id, "City : " + str(weatherData['city']) +'\nTemperature : ' 
                + str(weatherData['temp']) +'\nClouds : '
                + str(weatherData['clouds']) +'\nWind : '
                + str(weatherData['wind']['speed']))
            except:
                bot.send_message(message.chat.id, "Ошибка ввода")

    @bot.callback_query_handler(func = lambda call: True)
    def test2(call):
        if call.data == "weatherChoice":
            sendWeather(call.message)
        elif call.data == "helpChoice":
            sendHelp(call.message)
    
    bot.infinity_polling()

if __name__ == '__main__': 
    Main()
