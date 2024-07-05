import datetime as dt
from Model.Schedule import Schedule
from Model.ExamSchedule import ExamSchedule
from DB.DataBase import DataBase
# Singelton Klasse, da nur eine Instanz existieren soll und in anderen Klassen auf die seleben Attributwerte
# zugegriffen werden kann.


class Student:
    _instance = None
    schedule_list = []

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Student, cls).__new__(cls)
        return cls._instance

    def __init__(self, db, study_duration,
                 study_start_date, last_name=None, first_name=None, student_number=None):
        if not hasattr(self, "initialized"):
            from Model.Study import Study
            from Model.AvgGrade import AvgGrade
            if study_start_date is None:
                study_start_date = dt.date.today()
            self.db = db
            self.last_name = last_name
            self.first_name = first_name
            self.student_number = student_number
            self.study_duration = study_duration
            self.study_start_date = study_start_date
            self.study = Study(self.study_duration, self.study_start_date)
            self.student_moduls = self.study.modul_list
            self.avg_grade = AvgGrade()
            self.initialized = True
            self.id = None

    def save(self):
        if self.id is None:
            query = """
            INSERT INTO Student (last_name, first_name, student_number, study_duration, study_start_date)
            VALUES (%s, %s, %s, %s, %s)
            """
            params = (self.last_name, self.first_name, self.student_number, self.study_duration, self.study_start_date)
            self.db.execute_query(query, params)
            self.id = self.db.cursor.lastrowid
        else:
            query = """
            UPDATE Student
            SET last_name = %s, first_name = %s, student_number = %s, study_duration = %s, study_start_date
            WHERE id = %s
            """
            params = (self.last_name, self.first_name, self.student_number, self.study_duration, self.study_start_date,
                      self.id)
            self.db.execute_query(query, params)

    def load(self, student_id):
        query = "SELECT * FROM Student WHERE id = %s"
        params = (student_id,)
        result = self.db.fetch_one(query, params)
        if result:
            self.id = result['id']
            self.last_name = result['last_name']
            self.first_name = result['first_name']
            self.student_number = result['student_number']
            self.study_duration = result['study_duration']
            self.study_start_date = result['study_start_date']

    def delete(self):
        if self.id:
            query = "DELETE FROM Student WHERE id = %s"
            params = (self.id,)
            self.db.execute_query(query, params)
            self.id = None


    # Aktualisiert die Werte des Moduls
    def update_modul(self, modul_id, status=None, end_date=None, exam_date=None, grade=None):
        self.student_moduls[modul_id].acronym = status
        self.student_moduls[modul_id].end_date = end_date
        self.student_moduls[modul_id].exam_date = exam_date
        self.student_moduls[modul_id].grade = grade

    # Erstellt einen Termin und fügt ihn zur schedule_list hinzu
    def create_and_add_schedule(self, schedule_title, schedule_date):
        if isinstance(schedule_date, str):
            schedule_date = dt.datetime.strptime(schedule_date, "%d.%m.%Y %H:%M")
        schedule = Schedule(schedule_title, schedule_date)
        self.schedule_list.append(schedule)

    # Erstellt ein Klasusurtermin und fügt ihn zur schedule_list hinzu
    def create_and_add_exam_schedule(self, exam_schedule_title, exam_schedule_date):
        if isinstance(exam_schedule_date, str):
            exam_schedule_date = dt.datetime.strptime(exam_schedule_date, "%d.%m.%Y %H:%M")
        exam_schedule = ExamSchedule(exam_schedule_title, exam_schedule_date, None)
        self.schedule_list.append(exam_schedule)

    # Löscht einen Termin
    def remove_schedule(self, schedule_id):
        for schedul in self.schedule_list:
            if schedul.schedule_id == schedule_id:
                self.schedule_list.remove(schedul)
