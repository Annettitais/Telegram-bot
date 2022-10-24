import telebot
bot = telebot.TeleBot('5353009282:AAFIt6skOwhYAv-nirLHiKWvyQ-PUkhPAFk')

@bot.message_handler(content_types=['text'])
def start_text_class5(message):
    if message.text == "Натуральные числа и шкалы":
        bot.send_message(message.chat.id,
                         'Натуральные числа — это числа, которые мы используем для подсчета чего-то конкретного, осязаемого.')
        bot.send_message(message.chat.id,
                         'Вот какие числа называют натуральными: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 и т. д.')
        bot.send_message(message.chat.id, 'Натуральный ряд — последовательность всех натуральных чисел, '
                                               'расположенных в порядке возрастания. Первые сто можно посмотреть в таблице.')
        bot.send_photo(message.chat.id,
                       photo='https://user84060.clients-cdnnow.ru/uploads/5f9bad51bc22e760523687.png')
    if message.text == "Сложение и вычитание натуральных чисел":
        bot.send_message(message.chat.id, 'Сложение — операция, которая позволяет объединить два слагаемых.')
        bot.send_photo(message.chat.id,
                       photo='https://cdn-user84060.skyeng.ru/uploads/62377efb2d17a257733794.png')
        bot.send_message(message.chat.id, 'Вычитание — действие, обратное сложению.')
        bot.send_photo(message.chat.id,
                       photo='https://cdn-user84060.skyeng.ru/uploads/62377feed9a96594953254.png')
    if message.text == "Умножение и деление натуральных чисел":
        bot.send_message(message.chat.id,
                         'Умножение — арифметическое действие в виде краткой записи суммы одинаковых слагаемых.')
        bot.send_video(message.chat.id,
                       'https://upload.wikimedia.org/wikipedia/commons/3/32/Poser-une-multiplication.gif')
        bot.send_message(message.chat.id, 'Деление — арифметическое действие обратное умножению.')
        bot.send_photo(message.chat.id,
                       photo='https://cdn-user84060.skyeng.ru/uploads/623781da64c8e694543626.png')
