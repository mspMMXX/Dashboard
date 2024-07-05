# Datei: Model/Student.py
import datetime as dt
from Model.Schedule import Schedule
from Model.ExamSchedule import ExamSchedule


class Student:
    _instance = None
    schedule_list = []

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Student, cls).__new__(cls)
        return cls._instance

    def __init__(self, db, study_duration, study_start_date, last_name=None, first_name=None, student_number=None):
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

            self.id = None
            self.study = Study(self.db, self.study_duration, self.study_start_date, self.id)
            self.student_moduls = self.study.modul_list
            self.avg_grade = AvgGrade()
            self.schedule_list = []
            self.initialized = True

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
            SET last_name = %s, first_name = %s, student_number = %s, study_duration = %s, study_start_date = %s
            WHERE id = %s
            """
            params = (self.last_name, self.first_name, self.student_number, self.study_duration, self.study_start_date, self.id)
            self.db.execute_query(query, params)

    def load_schedules(self):
        query = "SELECT * FROM Schedule WHERE student_id = %s"
        params = (self.id,)
        results = self.db.fetch_all(query, params)
        for result in results:
            schedule = Schedule.from_dict(result)
            self.schedule_list.append(schedule)

    def create_and_add_schedule(self, schedule_title, schedule_date):
        if isinstance(schedule_date, str):
            schedule_date = dt.datetime.strptime(schedule_date, "%d.%m.%Y %H:%M")
        schedule = Schedule(self.db, schedule_title, schedule_date, self.id)
        self.schedule_list.append(schedule)
        schedule.save()

    # Erstellt ein Klasusurtermin und fügt ihn zur schedule_list hinzu
    def create_and_add_exam_schedule(self, exam_schedule_title, exam_schedule_date):
        if isinstance(exam_schedule_date, str):
            exam_schedule_date = dt.datetime.strptime(exam_schedule_date, "%d.%m.%Y %H:%M")
        exam_schedule = ExamSchedule(self.db, exam_schedule_title, exam_schedule_date, self.id)
        self.schedule_list.append(exam_schedule)
        exam_schedule.save()

    # Löscht einen Termin
    def remove_schedule(self, schedule_id):
        for schedul in self.schedule_list:
            if schedul.schedule_id == schedule_id:
                self.schedule_list.remove(schedule_id)
