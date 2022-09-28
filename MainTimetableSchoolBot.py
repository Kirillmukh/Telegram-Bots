import telebot
import time
from datetime import datetime


def GoHome():
    bot.send_message(Channel_Name, f"домой")


token = ""
bot = telebot.TeleBot(token)
Channel_Name = ""

week = {"Monday": (
    'Разговоры о важном', 'Алгебра', 'Литература', 'Информатика', 'Информатика', 'Биология', 'Физика', 'ИУП'),
    "Tuesday": (
        'Геометрия', 'Физика', 'Английский язык', 'Русский язык', 'Большие данные', 'Информатика', 'Алгебра'),
    "Wednesday": ('Алгебра', 'Геометрия', 'КАТ', 'Литература', 'История', 'Физкультура', 'Английский язык'),
    "Thursday": ('Английский язык', 'Рксский язык', 'Информатика', 'Литература', 'Алгебра', 'Программирование'),
    "Friday": ('Химия', 'История', 'ОБЖ', 'Программирование', 'Геометрия', 'Большие данные', 'Физкультура')}
while True:
    now = datetime.now()
    current_time = now.strftime("%H.%M")
    todaylist = week[time.strftime("%A")]
    if current_time == "08.05":
        bot.send_message(Channel_Name, f"{todaylist[0]} начнется в 8.30, 1 урок")
    if current_time == "09.15":
        bot.send_message(Channel_Name, f"{todaylist[1]} начнется в 9.30, 2 урок")
    if current_time == "10.15":
        bot.send_message(Channel_Name, f"{todaylist[2]} начнется в 10.35, 3 урок")
    if current_time == "11.20":
        bot.send_message(Channel_Name, f"{todaylist[3]} начнется в 11.30, 4 урок")
    if current_time == "12.15":
        bot.send_message(Channel_Name, f"{todaylist[4]} начнется в 12.35, 5 урок")
    if current_time == "13.20":
        bot.send_message(Channel_Name, f"{todaylist[5]} начнется в 13.40, 6 урок")
    if current_time == "14.25":
        if len(todaylist) >= 7:
            bot.send_message(Channel_Name, f"{todaylist[6]} начнется в 14.35, 7 урок")
        else:
            GoHome()
    if current_time == "15.20":
        if len(todaylist) == 8:
            bot.send_message(Channel_Name, f"{todaylist[7]} начнется в 15.30, 8 урок")
        elif len(todaylist) == 7:
            GoHome()
    if current_time == "16.15" and len(todaylist) == 8:
        GoHome()
    time.sleep(60)
