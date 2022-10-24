from telebot import types
from class5 import *
from class6 import *

bot = telebot.TeleBot('5353009282:AAFIt6skOwhYAv-nirLHiKWvyQ-PUkhPAFk')

@bot.message_handler(commands=["start","help"])
def welcome(message):
    hello = bot.send_message(message.chat.id,"Привет!")
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    class5 = types.KeyboardButton("5 класс")
    class6 = types.KeyboardButton("6 класс")
    class7 = types.KeyboardButton("7 класс")
    markup.add(class5, class6, class7)
    bot.send_message(message.chat.id, "Я помогу помочь тебе с темой по математике, но для этого ты должен выбрать класс!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def start_text(message):
    if message.text == "5 класс":
        tcl5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        tcl5_1 = types.KeyboardButton("Натуральные числа и шкалы")
        tcl5_2 = types.KeyboardButton("Сложение и вычитание натуральных чисел")
        tcl5_3 = types.KeyboardButton("Умножение и деление натуральных чисел")
        tcl5_4 = types.KeyboardButton("К выбору класса")
        tcl5.add(tcl5_1, tcl5_2, tcl5_3, tcl5_4)
        bot.send_message(message.chat.id,"Выбери тему или нажми 'К выбору класса' ",reply_markup=tcl5)
        ## 6 класс
    if message.text == "6 класс":
        tcl6 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        tcl6_1 = types.KeyboardButton("Делимость чисел")
        tcl6_2 = types.KeyboardButton("Сложение, вычитание, умножение и деление дробей")
        tcl6_3 = types.KeyboardButton("Отношения и пропорции")
        tcl6_4 = types.KeyboardButton("К выбору класса")
        tcl6.add(tcl6_1, tcl6_2, tcl6_3, tcl6_4)
        bot.send_message(message.chat.id,"Выбери тему или нажми 'К выбору класса' ",reply_markup=tcl6)
        ## 7 класс
    if message.text == "7 класс":
        tcl7 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        tcl7_1 = types.KeyboardButton("Натуральные числа и шкалы")
        tcl7_2 = types.KeyboardButton("Сложение и вычитание натуральных чисел")
        tcl7_3 = types.KeyboardButton("Умножение и деление натуральных чисел")
        tcl7_4 = types.KeyboardButton("К выбору класса")
        tcl7.add(tcl7_1, tcl7_2, tcl7_3, tcl7_4)
        bot.send_message(message.chat.id,"Выбери тему или нажми 'К выбору класса' ",reply_markup=tcl7)
    elif message.text == "К выбору класса":
        welcome(message)

    ##Если выбрана тема "Натуральные числа и шкалы"
    start_text_class5(message)
     ##Если выбрана тема "Сложение и вычитание натуральных чисел"
    start_text_class6(message)
    ##Если выбрана тема "Умножение и деление натуральных чисел"

bot.polling(none_stop=True)
