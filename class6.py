import telebot
from telebot import types
bot = telebot.TeleBot('5353009282:AAFIt6skOwhYAv-nirLHiKWvyQ-PUkhPAFk')

@bot.message_handler(commands=["start","help"])
def start6(message):
    tema6 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    tema6_1 = types.KeyboardButton("Делимость чисел")
    tema6_2 = types.KeyboardButton("Сложение, вычитание, умножение и деление дробей")
    tema6_3 = types.KeyboardButton("Отношения и пропорции")
    tema6_4 = types.KeyboardButton("К выбору класса")
    tema6.add(tema6_1, tema6_2, tema6_3, tema6_4)
    bot.send_message(message.chat.id, "Выберите тему или нажми 'К выбору класса'", reply_markup=tema6)

@bot.message_handler(content_types=['text'])
def start_text_class6(message):
    if message.text == "Делимость чисел":
        tcl61 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        tcl61_1 = types.KeyboardButton("Делители и кратные. Правила")
        tcl61_2 = types.KeyboardButton("Делимость чисел 2")
        tcl61_3 = types.KeyboardButton("Делимость чисел 3")
        tcl61_4 = types.KeyboardButton("Вернуться к выбору темы")
        tcl61.add(tcl61_1, tcl61_2, tcl61_3, tcl61_4)
        bot.send_message(message.chat.id, "Выбери подтему или нажми  'Вернуться к выбору темы' ", reply_markup=tcl61)
    if message.text == "Сложение, вычитание, умножение и деление дробей":
        bot.send_message(message.chat.id,
                         'Натуральные числа 2')
    if message.text == "Отношения и пропорции":
        bot.send_message(message.chat.id, 'Натуральные числа 3')
    elif message.text == "Вернуться к выбору темы": start6(message)

@bot.message_handler(content_types=['text'])
def del_class6(message):
    if message.text == "Делите и кратные. Правила":
        bot.send_message(message.chat.id, 'Делителем натурального числа n называют число, на которое n делится без остатка.')
        bot.send_photo(message.chat.id,
                       photo='https://ic.wampi.ru/2022/10/24/imageae230e915395a8c6.png')
        bot.send_message(message.chat.id,
                         ' Если число b делитель числа a , то a называют кратным числу b.')
        bot.send_photo(message.chat.id,
                       photo='https://ic.wampi.ru/2022/10/24/imagea5adfc04fafeba85.png')






