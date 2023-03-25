from datetime import datetime, date, timedelta
from random import randint
import sqlite3
from faker import Faker

fake = Faker("uk-UA")

disciplines = [
    "Системи тягового електропостачання",
    "Електропостачання рухомого складу",
    "Промислове електропостачання",
    "САПР",
    "Електропостачання нетягових споживачів",
    "Системи та мережі",
    "Тягові підстанції",
    "Електричні апарати",
    "Контактна мережа",
    "Автоматизація систем електропостачання"
]

groups = ["255", "256", "255M"]

NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 50

connect = sqlite3.connect("hw_6.sqlite")
cur = connect.cursor()


def seed_teachers():
    teachers = [fake.name() for _ in range(NUMBER_TEACHERS)]
    sql_ex = "INSERT INTO teachers(fullname) VALUES(?);"
    cur.executemany(sql_ex, zip(teachers, ))


def seed_groups():
    sql_ex = "INSERT INTO groups(name) VALUES(?);"
    cur.executemany(sql_ex, zip(groups, ))


def seed_disciplines():
    list_teacher_id = [randint(1, NUMBER_TEACHERS) for _ in range(len(disciplines))]
    sql_ex = "INSERT INTO disciplines(name, teacher_id) VALUES(?, ?);"
    cur.executemany(sql_ex, zip(disciplines, iter(list_teacher_id)))


def seed_students():
    students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    list_group_id = [randint(1, len(groups)) for _ in range(NUMBER_STUDENTS)]
    sql_ex = "INSERT INTO students(fullname, group_id) VALUES(?, ?);"
    cur.executemany(sql_ex, zip(students, iter(list_group_id)))


def seed_grades():
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-06-30", "%Y-%m-%d")
    sql_ex = "INSERT INTO grades(student_id, discipline_id, grade, date_of) VALUES(?, ?, ?, ?);"

    def get_list_of_date(start_date, end_date):
        result = []
        current_date = start_date
        while current_date <= end_date:
            if current_date.isoweekday() < 6:
                result.append(current_date)
            current_date += timedelta(1)
        return result

    list_dates = get_list_of_date(start_date, end_date)

    grades = []

    for day in list_dates:
        random_discipline = randint(1, len(disciplines))
        random_student = [randint(1, NUMBER_STUDENTS) for _ in range(5)]
        for student in random_student:
            grades.append((random_discipline, student, randint(1, 12), day.date()))
    cur.executemany(sql_ex, grades)


if __name__ == '__main__':
    try:
        seed_teachers()
        seed_groups()
        seed_disciplines()
        seed_students()
        seed_grades()
        connect.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        connect.close()
