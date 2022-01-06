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
        start_bot = bot.send_message(message.chat.id, 'Страрт работы бота')

    @bot.message_handler(commands=['weather'])
    def GetCityBot(message):
        bot.send_message(message.chat.id, "Введите город")
        bot.register_next_step_handler(message, GetDateBot)

    def GetDateBot(message):
        city = message.text
        menuInlineWeather = types.InlineKeyboardMarkup()
        todayButtonInline = types.InlineKeyboardButton(text = "сегодня", callback_data = "todayChoice")
        tommorowButtonInline = types.InlineKeyboardButton(text = "завтра", callback_data = "tommorowChoice")
        menuInlineWeather.add(todayButtonInline, tommorowButtonInline)
        bot.send_message(message.chat.id, "Выберите на когда хотите узнать прогноз (сегодня/завтра)", reply_markup = menuInlineWeather)
        
        bot.register_next_step_handler(message, GetWeatherBot, city)

    def GetWeatherBot(message, city):
        print(city, ' ', message.text)
        try:
            weatherData = GetWeather(city, message.text)
            bot.send_message(message.chat.id, "City : " + str(weatherData['city']) +
            "\ndate: " + str(weatherData['date']) +
            "\ntemp: " + str(weatherData['temp'])
            )
        except:
            bot.send_message(message.chat.id, "Ошибка ввода")   



    @bot.message_handler(commands=['help'])
    def sendHelp(message):
        bot.send_message(message.chat.id, "пока что без помощи")


    @bot.message_handler(commands=['import_github'])
    def secret(message):
        data = Secert()
        bot.send_message(message.chat.id, data)

    bot.infinity_polling()


if __name__ == '__main__': 
    Main()