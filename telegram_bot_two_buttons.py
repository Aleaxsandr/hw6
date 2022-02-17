# бот с двумя кнопками

# import telebot
# import random
# from telebot import types
# # Загружаем список интересных фактов
# f = open('data/facts.txt', 'r', encoding='UTF-8') # скопировать факты с интернета все должны быть с новой строки.
# facts = f.read().split('\n')
# f.close()
# # Загружаем список поговорок
# f = open('data/thinks.txt', 'r', encoding='UTF-8')# скопировать поговорки с интернета все должны быть с новой строки.
# thinks  = f.read().split('\n')
# f.close()
# # Создаем бота
# bot = telebot.TeleBot('5171900255:AAEDiX0IWW0RSnZksJxeEx1Ox9Efoj2Xahc')
# # Команда start
# @bot.message_handler(commands=["start"])
# def start(m, res=False):
#         # Добавляем две кнопки
#         markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#         item1=types.KeyboardButton("Факт")
#         item2=types.KeyboardButton("Поговорка")
#         markup.add(item1)
#         markup.add(item2)
#         bot.send_message(m.chat.id, 'Нажми: \nФакт для получения интересного факта\nПоговорка — для получения мудрой цитаты ',  reply_markup=markup)
# # Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     # Если юзер прислал 1, выдаем ему случайный факт
#     if message.text.strip() == 'Факт' :
#             answer = random.choice(facts)
#             bot.send_message(message.chat.id, answer)
#     # Если юзер прислал 2, выдаем умную мысль
#     elif message.text.strip() == 'Поговорка':
#             answer = random.choice(thinks)
#             bot.send_message(message.chat.id, answer)
#     # Отсылаем юзеру сообщение в его чат
#
# # Запускаем бота
# bot.polling(none_stop=True, interval=0)