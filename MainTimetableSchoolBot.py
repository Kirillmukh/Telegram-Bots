import telebot
import time
from datetime import datetime

token = ""
bot = telebot.TeleBot(token)
Channel_Name = ""

week = {"Monday": ('Разговоры о важном', 'Алгебра', 'Литература', 'Информатика', 'Информатика', 'Биология', 'Физика', 'ИУП'),
        "Tuesday": ('Геометрия', 'Физика', 'Английский язык', 'Русский язык', 'Большие данные', 'Информатика', 'Алгебра'),
        "Wednesday": ('Алгебра', 'Геометрия', 'КАТ', 'Литература', 'История', 'Физкультура', 'Английский язык'),
        "Thursday": ('Английский язык', 'Русский язык', 'Информатика', 'Литература', 'Алгебра', 'Программирование'),
        "Friday": ('Химия', 'История', 'ОБЖ', 'Программирование', 'Геометрия', 'Большие данные', 'Физкультура'),
        "Saturday": (),
        "Sunday": ()}
while True:
    now = datetime.now()
    current_time = now.strftime("%H.%M")
    todaylist = week[time.strftime("%A")]
    if not len(todaylist) == 0:
        match current_time:
            case "08.09":
                bot.send_message(Channel_Name, f"{todaylist[0]} начнется в 8.30, 1 урок")
            case "09.15":
                bot.send_message(Channel_Name, f"{todaylist[1]} начнется в 9.30, 2 урок")
            case "10.15":
                bot.send_message(Channel_Name, f"столовая, {todaylist[2]} начнется в 10.35, 3 урок")
            case "11.20":
                bot.send_message(Channel_Name, f"{todaylist[3]} начнется в 11.30, 4 урок")
            case "12.15":
                bot.send_message(Channel_Name, f"{todaylist[4]} начнется в 12.35, 5 урок")
            case "13.20":
                if len(todaylist) == 6:
                    bot.send_message(Channel_Name, f"столовая, последний урок - {todaylist[5]} начнется в 13.40, 6 урок")
                else:
                    bot.send_message(Channel_Name,f"столовая, {todaylist[5]} начнется в 13.40, 6 урок")
            case "14.25":
                if len(todaylist) == 7:
                    bot.send_message(Channel_Name, f"последний урок -  {todaylist[6]} начнется в 14.35, 7 урок")
                else:
                    bot.send_message(Channel_Name, f"{todaylist[6]} начнется в 14.35, 7 урок")
            case "15.20":
                if len(todaylist) == 8:
                    bot.send_message(Channel_Name, f"последний урок - {todaylist[7]} начнется в 15.30, 8 урок")
        time.sleep(60)
    else:
        time.sleep(82800)
