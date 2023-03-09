import sqlite3
from os import system


con = sqlite3.connect('schedule_group.sqlite')
cur = con.cursor()


def create_table():
    cur.execute('''
    CREATE TABLE IF NOT EXISTS schedule_data(
    id INTEGER PRIMARY KEY,
    now_week INTEGER,
    now_day INTEGER,
    lesson TEXT,
    start_time TEXT,
    end_time TEXT,
    date TEXT,
    rooms TEXT,
    type_lesson TEXT
    );
    ''')


def add_first_information(now_week: int, now_day: int,
                          lesson: str, start_time: str,
                          end_time: str, date: str,
                          rooms: str, type_lesson: str) -> None:
    add_data = [(0, now_week, now_day, lesson,
                 start_time, end_time, date, rooms,
                 type_lesson)]
    cur.executemany('INSERT INTO schedule_data VALUES(?,?,?,?,?,?,?,?,?);',
                    add_data)


def add_information(now_week: int, now_day: int,
                    lesson: str, start_time: str,
                    end_time: str, date: str,
                    rooms: str, type_lesson: str) -> None:
    cur.execute('''
    SELECT MAX(id)
    FROM schedule_data
    ''')
    max_id = int(cur.fetchone()[0]) + 1
    add_data = [(max_id, now_week, now_day, lesson,
                 start_time, end_time, date, rooms,
                 type_lesson)]
    cur.executemany('INSERT INTO schedule_data VALUES(?,?,?,?,?,?,?,?,?);',
                    add_data)


def all_data():
    cur.execute('''
    SELECT *
    FROM schedule_data
    ''')
    for res in cur:
        print(res)


def all_tables():
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return cur.fetchall()


if __name__ == '__main__':
    try:
        create_table()
        add_first_information(1, 1, 'test', 'test', 'test', 'test', 'test', 'test')
        system('python get_timetable.py')
    except sqlite3.IntegrityError:
        print('таблица с расписанием уже существет')


con.commit()
