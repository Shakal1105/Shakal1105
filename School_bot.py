import telebot
from time import sleep

bot = telebot.TeleBot('1687493227:AAEeNBiC4jA7iFu-e2tH_dhTu1eMWhovCu4')

monday_lessons = {0:'Нулевой урок',
                  1:'первый урок',
                  2:"второй урок",
                  3:'третий урок',
                  4:'четвёртый урок',
                  5:'пятый урок',
                  6:'шестой урок',
                  7:'седьмой урок',
                  8:'восьмой урок'}
tuesday_lessons = {0:'Нулевой урок',
                  1:'первый урок',
                  2:"второй урок",
                  3:'третий урок',
                  4:'четвёртый урок',
                  5:'пятый урок',
                  6:'шестой урок',
                  7:'седьмой урок',
                  8:'восьмой урок'}
wednesday_lessons = {0:'Нулевой урок',
                  1:'первый урок',
                  2:"второй урок",
                  3:'третий урок',
                  4:'четвёртый урок',
                  5:'пятый урок',
                  6:'шестой урок',
                  7:'седьмой урок',
                  8:'восьмой урок'}
thursday_lessons = {0:'Нулевой урок',
                  1:'первый урок',
                  2:"второй урок",
                  3:'третий урок',
                  4:'четвёртый урок',
                  5:'пятый урок',
                  6:'шестой урок',
                  7:'седьмой урок',
                  8:'восьмой урок'}
friday_lessons = {0:'Нулевой урок',
                  1:'первый урок',
                  2:"второй урок",
                  3:'третий урок',
                  4:'четвёртый урок',
                  5:'пятый урок',
                  6:'шестой урок',
                  7:'седьмой урок',
                  8:'восьмой урок'}
saturday_lessons = 'Выходной день'
sunday_lessons = 'Выходной день'

stringlesson = ("0 => 8:00 - 8:45 \n1 => 9:00 - 9:45 \n2 => 9:55 - 10:40 \n3 => 11:00 - 11:45 \n4 => 12:05 - 12:50 \n5 => 13:00 - 13:45 \n6 => 13:55 - 14:40 \n7 => 14:50 - 15:35")

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Приятного пользования🙄, мы в телеграм @shakal11052002 and @LParub')

@bot.message_handler(commands=['help'])
def campain(message):
    bot.send_message(message.chat.id, "use commands: \n /lessonbom /lessonweek or введите текст Понедельник, ВтОрНик и тд от больших и малых букв ошибки не будет ")

@bot.message_handler(commands=['lessonbom'])
def lessbom(message):
    bot.send_message(message.chat.id, "Please:")
    bot.send_message(message.chat.id, stringlesson)



@bot.message_handler(commands=['lessonweek'])
def lessbom(message):
    bot.send_message(message.chat.id, "Понедельник:")
    for result in monday_lessons:
        bot.send_message(message.chat.id, f'{str(result)} ==> {str(monday_lessons[result])}')
    sleep(1)
    bot.send_message(message.chat.id, "Вторник:")
    for result in tuesday_lessons:
        bot.send_message(message.chat.id, f'{str(result)} ==> {str(tuesday_lessons[result])}')
    sleep(1)
    bot.send_message(message.chat.id, "Среда:")
    for result in wednesday_lessons:
        bot.send_message(message.chat.id, f'{str(result)} ==> {str(wednesday_lessons[result])}')
    sleep(1)
    bot.send_message(message.chat.id, "Четверг:")
    for result in thursday_lessons:
        bot.send_message(message.chat.id, f'{str(result)} ==> {str(thursday_lessons[result])}')
    sleep(1)
    bot.send_message(message.chat.id, "Пятница:")
    for result in friday_lessons:
        bot.send_message(message.chat.id, f'{str(result)} ==> {str(friday_lessons[result])}')
    sleep(1)
    bot.send_message(message.chat.id, f'Субота:\n{saturday_lessons}')
    sleep(1)
    bot.send_message(message.chat.id, f'Воскресенье:\n{sunday_lessons}')

bot.polling()