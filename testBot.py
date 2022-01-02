import telebot
from Sourses import config


def Main():

    bot = telebot.TeleBot(config['API_KEI'])

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "new Test message")


    bot.infinity_polling()

if __name__ == '__main__':
    Main()
