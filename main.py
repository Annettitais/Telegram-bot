import telebot

bot = telebot.TeleBot('5353009282:AAFIt6skOwhYAv-nirLHiKWvyQ-PUkhPAFk')


@bot.message_handler(commands=['start', 'help'])
def process_start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    keyboard.row('Начать!')
    msg = bot.send_message(message.chat.id, text='Привет! В каком ты классе?', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def step1(message):
    menu1 = telebot.types.InlineKeyboardMarkup()
    menu1.add(telebot.types.InlineKeyboardButton(text='5 класс', callback_data='class5'))
    menu1.add(telebot.types.InlineKeyboardButton(text='6 класс', callback_data='class6'))
    menu1.add(telebot.types.InlineKeyboardButton(text='7 класс', callback_data='class7'))
    if message.text == 'Начать!':
        msg = bot.send_message(message.chat.id, text='Выбери класс!', reply_markup=menu1)


@bot.callback_query_handler(func=lambda call: True)
def step2(call):
    menu2 = telebot.types.InlineKeyboardMarkup()
    menu2.add(telebot.types.InlineKeyboardButton(text='Натуральные числа и шкалы', callback_data='class5_1'))
    menu2.add(
        telebot.types.InlineKeyboardButton(text='Сложение и вычитание натуральных чисел', callback_data='class5_2'))
    menu2.add(
        telebot.types.InlineKeyboardButton(text='Умножение и деление натуральных чисел', callback_data='class5_3'))
    if call.data == 'class5':
        msg = bot.send_message(call.message.chat.id, 'С какой темой нужно помочь?', reply_markup=menu2)
    if call.data == 'class5_1':
        bot.send_message(call.message.chat.id,
                         'Натуральные числа — это числа, которые мы используем для подсчета чего-то конкретного, осязаемого.')
        bot.send_message(call.message.chat.id,
                         'Вот какие числа называют натуральными: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 и т. д.')
        bot.send_message(call.message.chat.id, 'Натуральный ряд — последовательность всех натуральных чисел, '
                                               'расположенных в порядке возрастания. Первые сто можно посмотреть в таблице.')
        bot.send_photo(call.message.chat.id,
                       photo='https://user84060.clients-cdnnow.ru/uploads/5f9bad51bc22e760523687.png')
    if call.data == 'class5_2':
        bot.send_message(call.message.chat.id, 'Сложение — операция, которая позволяет объединить два слагаемых.')
        bot.send_photo(call.message.chat.id,
                       photo='https://cdn-user84060.skyeng.ru/uploads/62377efb2d17a257733794.png')
        bot.send_message(call.message.chat.id, 'Вычитание — действие, обратное сложению.')
        bot.send_photo(call.message.chat.id,
                       photo='https://cdn-user84060.skyeng.ru/uploads/62377feed9a96594953254.png')
    if call.data == 'class5_3':
        bot.send_message(call.message.chat.id,
                         'Умножение — арифметическое действие в виде краткой записи суммы одинаковых слагаемых.')
        bot.send_video(call.message.chat.id,
                       'https://upload.wikimedia.org/wikipedia/commons/3/32/Poser-une-multiplication.gif')
        bot.send_message(call.message.chat.id, 'Деление — арифметическое действие обратное умножению.')
        bot.send_photo(call.message.chat.id,
                       photo='https://cdn-user84060.skyeng.ru/uploads/623781da64c8e694543626.png')
    if call.data == 'class6':
        bot.send_message(call.message.chat.id, 'Пожалуйста, выбери 5 класс! 6 класс еще в работе :)')
    if call.data == 'class7':
        bot.send_message(call.message.chat.id, 'Пожалуйста, выбери 5 класс! 7 класс еще в работе :)')
    bot.send_message(call.message.chat.id, 'Чтобы вернуться в начало, примените команду /start')

bot.polling()
