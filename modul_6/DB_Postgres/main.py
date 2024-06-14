import logging

from faker import Faker
import random
import psycopg2
from psycopg2 import sql, DatabaseError

fake = Faker()

# Соединяемся с базой данных
conn = psycopg2.connect(host='localhost', database="test", user="postgres", password="0000")

# Создаем курсор для выполнения SQL-запросов
cur = conn.cursor()

# Генерируем случайные данные для групп
for i in range(1, 4):
    cur.execute(
        "INSERT INTO groups (name) VALUES (%s)",
        (fake.word(),)
    )

# Генерируем случайные данные для викладачей
for _ in range(1, 4):
    cur.execute(
        "INSERT INTO teachers (fullname) VALUES (%s)",
        (fake.name(),)
    )

# Генерируем случайные данные для предметов
for teacher_id in range(1, 4):
    for _ in range(2):
        cur.execute(
            "INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)",
            (fake.word(), teacher_id)
        )

'''
# Генерируем случайные данные для студентов
for _ in range(1, 31):
    cur.execute(
        "INSERT INTO students (fullname, group_id) VALUES (%s, %s)",
        (fake.name(), random.randint(1, 3))
    )

# Генерируем случайные данные для оценок

for student_id in range(1, 31):
    for subject_id in range(1, 4):
        for _ in range(random.randint(1, 4)):
            cur.execute(
                "INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (%s, %s, %s, %s)",
                (student_id, subject_id, random.randint(1, 5), fake.date_this_year())
            )
'''

for group_id in range(1, 4):
    for _ in range(10):
        cur.execute(
            'INSERT INTO students (fullname, group_id) VALUES (%s, %s) RETURNING id',
            (fake.name(), group_id)
        )
        student_id = cur.fetchone()[0]

        for subject_id in range(1, 7):
            for _ in range(3):
                cur.execute(
                    "INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (%s, %s, %s, %s)",
                    (student_id, subject_id, random.randint(1, 100), fake.date_this_decade())
                )


try:
    # Фиксируем изменения
    conn.commit()
except DatabaseError as e:
    logging.error(e)
    conn.rollback()
finally:
    # Закрываем соединение с базой данных
    cur.close()
    conn.close()
