import datetime

import psycopg2


def create_db():
    global cur
    global conn
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Course (
    id serial PRIMARY KEY NOT NULL,
    name varchar(100) NOT NULL);
    
    CREATE TABLE IF NOT EXISTS Student (
    id serial PRIMARY KEY NOT NULL,
    name varchar(100) NOT NULL,
    gpa numeric(10, 2),
    birth timestamp with time zone,
    course_id INTEGER REFERENCES COURSE(id));
    """)


def get_student(student_id):
    global cur
    global conn
    cur.execute("""SELECT * FROM Student
    WHERE id = (%s)""", (student_id,))
    cur.fetchall()


def get_students(course_id):
    global cur
    global conn
    cur.execute("""SELECT * FROM Student
    WHERE course_id = (%s);""", (course_id,))
    return cur.fetchall()


def add_student(student, course_id=None):
    global cur
    global conn
    sql = """INSERT INTO student
    (name, gpa, birth, course_id) values (%s, %s, %s, %s);"""
    cur.execute(sql, (*student, course_id))


def add_students(course_id, students):
    global cur
    global conn
    for student in students:
        add_student(student, course_id=course_id)


if __name__ == '__main__':
    with psycopg2.connect("dbname=guillotine_db user=guillotine") as conn:
        with conn.cursor() as cur:
            now = datetime.datetime.now()
            long_ago = now - datetime.timedelta()
            # print(get_student(1))
            # add_student(('Андрей', 5, long_ago, 1))
            # add_students(1, (('Алина', 4, long_ago), ('Матвей', 3, long_ago)))
            print(get_students(1))
