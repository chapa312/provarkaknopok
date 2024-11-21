import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


TOKEN = '7705299231:AAEDgGp4OtpjJJNhPchDjFaYwUBsrDe6lGA'
bot = telebot.TeleBot(TOKEN)


# Начальное меню
@bot.message_handler(commands=['start'])
def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Посмотреть услуги🔥")
    markup.add("Сделать заказ💳" )
    markup.add("О нас📜" )
    bot.send_message(message.chat.id, "Здравствуйте 👋! Я - Шлюха👯, бот прачечной ЯГАНДОН🔞 и Ваш верный помощник в мире чистоты!  Выберите действие которое Вас интересует", reply_markup=markup)

def back_button():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Назад"))
    return keyboard

# Посмотреть услуги
@bot.message_handler(func=lambda message: message.text == "Посмотреть услуги🔥")
def consulting_services(message):
    bot.send_message(message.chat.id, "Прачечная ЯГАНДОН🔞 занимаемся немалым спектром услуг в области стирки 🧺. В списке ниже Вы можете воспользоваться любой из представленных👇. Для заказа просто нажмите кнопку 'назад' и выберете меню 'Сделать заказ💳'" 
            
            "1. Стирка одежды\n"
            "2. Химчистка\n"
            "3. Услуги по глажке\n"
            "4. Стирка ковров\n"
            "5. Прачечная самообслуживания\n"
            "6. Уборка текстиля\n"
            "7. Доставка и забор одежды")



# сделать заказ
@bot.message_handler(func=lambda message: message.text == "Сделать заказ💳")
def consulting_services(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Стирка одежды")
    markup.add("Выведение пятен")
    markup.add("хуйчистка")
    bot.send_message(message.chat.id,"Прекрасно✨! Пожалуйста, выберите, что именно Вас интересует из списка ниже 👇")


# Стирка
@bot.message_handler(func=lambda message: message.text == "Стирка одежды")
def consulting_services(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("По весу", "По количеству")
    bot.send_message(message.chat.id, "Прекрасно! Наша компания производит постирку исходя из 2-х типов расчета: По весу (от 1кг), По количеству вещей. Выберете удобный для Вас формат", reply_markup=markup)






# возврат
# Обработка кнопки Назад
@bot.message_handler(func=lambda message: message.text == "Назад")
def go_back(message):
    main_menu(message)


bot.polling()