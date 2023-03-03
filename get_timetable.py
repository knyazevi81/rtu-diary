from requests import get

read = get('https://schedule.mirea.ninja/api/schedule/%'
           'D0%91%D0%91%D0%91%D0%9E-04-21/full_schedule')
last_week = get('https://schedule.mirea.ninja/api/schedule/current_week')


def get_week_lessons(date: int):
    data: dict = read.json()
    day_of_week = {
        '1': 'понедельник',
        '2': 'вторник',
        '3': 'среда',
        '4': 'четверг',
        '5': 'пятница',
        '6': 'суббота',
        '7': 'восскресенье'
    }

    print(day_of_week[str(1)])
    print(data['schedule'][str(1)]['lessons'][1][1]['name'])
    #if date in data['schedule'][str(i)]['lessons'][0]['weeks']:


if __name__ == '__main__':
    get_week_lessons(last_week.json()['week'])
