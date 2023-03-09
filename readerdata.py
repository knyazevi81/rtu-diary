import sqlite3

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
    rooms TEXT
    type_lesson TEXT
    );
    ''')


def add_information(now_week: int, now_day: int,
                    lesson: str, start_time: str,
                    end_time: str, date: str,
                    rooms: str, type_lesson: str) -> None:
    cur.execute('''
    SELECT MAX(id)
    FROM schedule_data
    ''')
    max_id = cur.fetchone()[0]
    add_data = [(now_week, now_day, lesson,
                 start_time, end_time, date, rooms,
                 type_lesson)]
    cur.executemany('INSERT INTO schedule_data VALUES(?,?,?,?,?,?,?,?);',
                    add_data)


def all_data():
    cur.execute('''
    SELECT id, *
    FROM schedule_data
    ''')
    for res in cur:
        print(res)


def all_tables():
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cur.fetchall())


if __name__ == '__main__':
    add_information(129291, 1, 'text', 'data', 'text', 'text', 'text', 'text')
    all_data()

con.commit()
