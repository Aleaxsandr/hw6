import telebot
import time
# Токен, который выдает @botfather
bot = telebot.TeleBot('5168194149:AAG6tXiEuJkxVSbSRx1tN9x0a2bM2wsrJn4')
# Адрес телеграм-канала, начинается с @
CHANNEL_NAME = '@hihinew1204'
# Загружаем список шуток
f = open('data/fun.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()
# Пока не закончатся шутки, посылаем их в канал
for joke in jokes:
    bot.send_message(CHANNEL_NAME, joke)
    # Делаем паузу в один час
    time.sleep(3600)
bot.send_message(CHANNEL_NAME, "Анекдоты закончились :-(")
