# coder: knyazevi81
# project: rtu-diary
# Модуль проекта по определению предетов по заданным параметрам
# и внесения в базу данных

from requests import get
import sqlite3
import datetime
from readerdata import add_information
from tokens import groupapi
from tokens import currentweekapi

read = get(groupapi)
last_week = get(currentweekapi)
data: dict = read.json()
now_week: int = last_week.json()['week']
con = sqlite3.connect('')


def calculate_day_by_week(now_day: int, now_week: int) -> datetime:
    """Функция определения даты."""
    start_date: datetime.date = datetime.date(2023, 2, 6)
    delta: datetime.timedelta = datetime.timedelta(days=7 * (now_week - 1)
                                                   + now_day - 1)
    return start_date + delta


def parse_api_to_data(now_day: int, now_week: int):
    """Перебор пар по типо дня недели."""
    day: str = str(now_day)
    try:
        for i in range(len(data['schedule'][day]['lessons'])):
            for j in range(len(data['schedule'][day]['lessons'][i])):
                if now_week in data['schedule'][day]['lessons'][i][j]['weeks']:
                    date: str = calculate_day_by_week(now_day, now_week)
                    lesson: str = data['schedule'][day]['lessons'][i][j]['name']
                    type_lesson: str = data['schedule'][day]['lessons'][i][j]['types']
                    rooms: str = data['schedule'][day]['lessons'][i][j]['rooms'][0]
                    start_time: str = data['schedule'][day]['lessons'][i][j]['time_start']
                    end_time: str = data['schedule'][day]['lessons'][i][j]['time_end']
                    add_information(now_week, now_day, lesson, start_time,
                                    end_time, date, rooms, type_lesson)
    except KeyError:
        print('Выходные')


if __name__ == '__main__':
    for now_week in range(1, 3):
        for now_day in range(1, 7):
            parse_api_to_data(now_day, now_week)
