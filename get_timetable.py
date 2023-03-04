# coder: knyazevi81
# project: rtu-diary
# Модуль проекта по определению предетов по заданным параметрам
# и внесения в базу данных

from requests import get
from tokens import groupapi
from tokens import currentweekapi

read = get(groupapi)
last_week = get(currentweekapi)
data: dict = read.json()
now_week: int = last_week.json()['week']


def parse_api(now_day: int, now_week: int) -> str:
    """Перебор пар по типо дня недели."""
    day: str = str(now_day)
    try:
        for i in range(len(data['schedule'][day]['lessons'])):
            for j in range(len(data['schedule'][day]['lessons'][i])):
                if now_week in data['schedule'][day]['lessons'][i][j]['weeks']:
                    print(data['schedule'][day]['lessons'][i][j]['name'],
                          data['schedule'][day]['lessons'][i][j]['types'],
                          data['schedule'][day]['lessons'][i][j]['time_start'],
                          '-',
                          data['schedule'][day]['lessons'][i][j]['time_end'])
    except KeyError:
        print('выходные')


def date_lessons(now_day: int, now_week: int):
    """Функция определения даты."""
    day: str = str(now_day)
    print(data['schedule'][day]['lessons'])


if __name__ == '__main__':
    parse_api(4, 1)
