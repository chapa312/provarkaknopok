# Ne donor

import telebot
from telebot import types
import sqlite3
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


 #Создание базы данных
def create_db():
    conn = sqlite3.connect('laundry_orders.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        service TEXT)''')
    conn.commit()
    conn.close()

create_db()
# Инициализация бота
TOKEN = '7705299231:AAEDgGp4OtpjJJNhPchDjFaYwUBsrDe6lGA'
bot = telebot.TeleBot(TOKEN)


# Начальное меню
@bot.message_handler(commands=['start'])

def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Посмотреть услуги🔥")
    markup.add("Сделать заказ💳")
    markup.add("Подробнее рассказать о прачечной ЯГАНДОН🔞📜")
    photo_url = 'https://ltdfoto.ru/image/meix0s'
        # Отправляем изображение
    bot.send_photo(message.chat.id, photo_url, caption="Здравствуйте 👋! Я - Шлюха👯, бот прачечной ЯГАНДОН🔞 и Ваш виртуальный помощник в мире чистоты!\n"
                                      "\n"
                                      "Помогу разобраться с услугами и подобрать подходящий для Вас вариант\n"
                                      "Доверьте мне заботу о чистоте и свежести ваших вещей! Чем могу быть полезна?",reply_markup=markup)
    #bot.send_message(message.chat.id, "Здравствуйте 👋! Я - Шлюха👯, бот прачечной ЯГАНДОН🔞 и Ваш верный помощник в мире чистоты!\n"
                                     # "\n"
                                      #"Выберите действие которое Вас интересует", reply_markup=markup)

def handle_message(message):
    if message.text == 'Посмотреть услуги🔥' or message.text == 'Кнопка 2':
        bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=message.message_id, reply_markup=None)

@bot.message_handler(func=lambda message: message.text == "Посмотреть услуги🔥")
def consulting_services(message):
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Назад", callback_data='button1')
    keyboard.add(button1)
    bot.send_message(message.chat.id, "Прачечная ЯГАНДОН🔞 занимаемся немалым спектром услуг в области стирки 🧺. В списке ниже Вы можете воспользоваться любой из представленных👇.\n" 
            " \n"
            "1. Стирка одежды\n"
            "2. Химчистка\n"
            "3. Услуги по глажке\n"
            "4. Стирка ковров\n"
            "5. Чистка кроссовок\n"
            "6. Стирка текстиля\n"
            "\n"
            " Для заказа просто нажмите 'Сделать заказ💳'\n",reply_markup=keyboard)



# обработка кнопки назад
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'button1':
        main_menu(call.message)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=main_menu())



# сделать заказ
@bot.message_handler(func=lambda message: message.text == "Сделать заказ💳")
def servises_services(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Стирка одежды")
    markup.add("Выведение пятен")
    markup.add("хуйчистка")
    markup.add("Назад")
    bot.send_message(message.chat.id,"Прекрасно✨! Пожалуйста, выберите, что именно Вас интересует из списка ниже 👇",reply_markup=markup)


# Обработка кнопки Назад
@bot.message_handler(func=lambda message: message.text == "Назад")
def go_back(message):
    main_menu(message)



# Стирка
@bot.message_handler(func=lambda message: message.text == "Стирка одежды")
def stirka_services(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("По весу", "По количеству")
    bot.send_message(message.chat.id, "Да, конечно!\n"
                                      "Прачечная ЯГАНДОН🔞 предоставляет услуги стирки исходя из 2-х типов расчета: По весу (от 1кг), По количеству вещей. Выберете удобный для Вас формат", reply_markup=markup)



# Выведение пятен
@bot.message_handler(func=lambda message: message.text == "Выведение пятен")
def pytna_services(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Назад🔙")
    bot.send_message(message.chat.id, "Прекрасно! Пятновыводкой мы занимаемся крайне хуёво, не советую", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "Назад🔙")
def go_back(message):
    servises_services(message)


# хуйчистка
@bot.message_handler(func=lambda message: message.text == "хуйчистка")
def huichistha(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Назад🔙")
    bot.send_message(message.chat.id, "Ой бля, сам себе хуй почистишь", reply_markup=markup)



@bot.message_handler(func=lambda message: True)
def handle_service_selection(message):
    service = message.text
    if service in ["По весу"]:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Назад")

        # Сохранение заказа в базе данных
        conn = sqlite3.connect('laundry_orders.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders (user_id, service) VALUES (?, ?)", (message.from_user.id, service))
        conn.commit()
        conn.close()

        bot.send_message(message.chat.id, f"Вы выбрали услугу: {service}. Ваш заказ принят! Для выхода в главное меню нажмите 'назад'",reply_markup=markup)

    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите одну из предложенных услуг.")


bot.polling(none_stop=True)