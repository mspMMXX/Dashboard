from Student import Student
from Study import Study
from datetime import datetime, timedelta


class Modul:

    def __init__(self, modul_id, acronym, title, exam_format, image):
        self.modul_id = modul_id
        self.acronym = acronym
        self.title = title
        self.exam_format = exam_format
        self.image = image
        self.status = "Offen"
        self.start_date = self.set_start_date()
        self.end_date = None
        self.deadline = self.set_deadline()
        self.exam_date = None
        self.grade = None
        self.student = Student
        self.study = Study

    def set_status(self, status):
        self.status = status

    def set_start_date(self):
        if self.status is "In Bearbeitung":
            return datetime.now()
        else:
            return None

    def set_end_date(self, end_date):
        self.end_date = end_date

    def set_deadline(self):
        time_for_modul = self.study.study_duration * 365 / 36
        if self.start_date:
            deadline_date = self.start_date + timedelta(days=time_for_modul)
            return deadline_date
        else:
            return None

    def set_exam_date(self, exam_date):
        self.exam_date = exam_date
        if self.student:
            self.student.create_and_add_exam_schedule(self.title, exam_date)

    def set_grade(self, grade):
        self.grade = grade
