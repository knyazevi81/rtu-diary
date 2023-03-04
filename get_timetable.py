# coder: knyazevi81
# project: rtu-diary
# Модуль проекта по определению предетов по заданным параметрам
# и внесения в базу данных

from requests import get
import datetime
from tokens import groupapi
from tokens import currentweekapi

read = get(groupapi)
last_week = get(currentweekapi)
data: dict = read.json()
now_week: int = last_week.json()['week']


def calculate_day_by_week(now_day: int, now_week: int) -> datetime.time:
    """Функция определения даты."""
    start_date = datetime.date(2023, 2, 6)
    delta = datetime.timedelta(days=7 * (now_week - 1) + now_day - 1)
    return start_date + delta


def parse_api(now_day: int, now_week: int) -> str:
    """Перебор пар по типо дня недели."""
    day: str = str(now_day)
    print(calculate_day_by_week(now_day, now_week))
    try:
        for i in range(len(data['schedule'][day]['lessons'])):
            for j in range(len(data['schedule'][day]['lessons'][i])):
                if now_week in data['schedule'][day]['lessons'][i][j]['weeks']:
                    print(data['schedule'][day]['lessons'][i][j]['name'],
                          data['schedule'][day]['lessons'][i][j]['types'],
                          data['schedule'][day]['lessons'][i][j]['rooms'][0],
                          data['schedule'][day]['lessons'][i][j]['time_start'],
                          '-',
                          data['schedule'][day]['lessons'][i][j]['time_end'])
    except KeyError:
        print('Выходные')


if __name__ == '__main__':
    parse_api(1, now_week)
