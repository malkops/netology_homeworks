import datetime

import psycopg2


class WorkWithPostgre:
    def __init__(self, dbname: str, username: str, pwd=''):
        self.dbname = dbname
        self.user = username
        self.pwd = pwd
        self.conn, self.cur = self.get_connection()

    def get_connection(self):
        conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.pwd)
        conn.autocommit = True
        cur = conn.cursor()

        return conn, cur

    def create_db(self) -> None:
        self.cur.execute("""
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

    def get_student(self, student_id: int) -> dict:
        self.cur.execute("""SELECT * FROM Student
        WHERE id = (%s)""", (student_id,))
        return self.cur.fetchall()

    def get_students(self, course_id: int) -> dict:
        self.cur.execute("""SELECT * FROM Student
        WHERE course_id = (%s);""", (course_id,))
        return self.cur.fetchall()

    def add_student(self, student: tuple, course_id=None) -> None:
        sql = """INSERT INTO student
        (name, gpa, birth, course_id) values (%s, %s, %s, %s);"""
        self.cur.execute(sql, (*student, course_id))

    def add_students(self, course_id: int, students: tuple) -> None:
        for student in students:
            self.add_student(student, course_id=course_id)


if __name__ == '__main__':
    connection_to_db = WorkWithPostgre(dbname='guillotine_db', username='guillotine')
    now = datetime.datetime.now()
    long_ago = now - datetime.timedelta()
    print(connection_to_db.get_student(5))
