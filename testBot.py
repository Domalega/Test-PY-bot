from pickle import TRUE
import telebot
from telebot import types
from telebot.types import InlineKeyboardButton, Message
from weatherparse import *
from Sourses import configForBot


def Main():
    bot = telebot.TeleBot(configForBot['API_BOT'])

    @bot.message_handler(commands=['start'])
    def Welcome(message):
        start_bot = bot.send_message(message.chat.id, 'Страрт работы бота')

    @bot.message_handler(commands=['weather'])
    def GetCityBot(message):
        bot.send_message(message.chat.id, "Введите город")
        bot.register_next_step_handler(message, GetDateBot)

    def GetDateBot(message):
        city = message.text
        bot.send_message(message.chat.id, "Выберите на когда хотите узнать прогноз (сегодня/завтра)")
        bot.register_next_step_handler(message, GetWeatherBot, city)

    def GetWeatherBot(message, city):
        try:
            weatherData = GetWeather(city, message.text)
            bot.send_message(message.chat.id, "City : " + str(weatherData['city']) +
            "\ndate: " + str(weatherData['date']) +
            "\ntemp: " + str(weatherData['temp'])
            )
        except:
            bot.send_message(message.chat.id, "Ошибка ввода")   

    @bot.message_handler(commands=['help'])
    def Help(message):
        bot.send_message(message.chat.id, "пока что без помощи")

    @bot.message_handler(commands=['import_github'])
    def Secret(message):
        data = Secert()
        bot.send_message(message.chat.id, data)

    bot.infinity_polling()


if __name__ == '__main__': 
    Main()