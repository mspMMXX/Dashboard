from Student import Student
from datetime import datetime, timedelta


class Modul:

    def __init__(self, modul_id, acronym, title, exam_format, image):
        self.modul_id = modul_id
        self.acronym = acronym
        self.title = title
        self.exam_format = exam_format
        self.image_path = image
        self.status = "Offen"
        self.start_date = self.set_start_date()
        self.end_date = None
        self.deadline = self.set_deadline()
        self.exam_date = None
        self.grade = None
        self.student = Student()

    # Setzen des Status
    def set_status(self, status):
        self.status = status

    # Setzen des Modulbeginns
    def set_start_date(self):
        if self.status is "In Bearbeitung":
            return datetime.now()
        else:
            return None

    # Wann das Modul abgeschlossen wurde
    def set_end_date(self, end_date):
        self.end_date = end_date

    # Generiert die Deadline bis wann das Modul abgeschlossen werden muss
    def set_deadline(self):
        time_for_modul = self.student.study.study_duration * 365 / 36
        if self.start_date:
            deadline_date = self.start_date + timedelta(days=time_for_modul)
            return deadline_date
        else:
            return None

    # Setzt das Prüfungsdatum und erstellt einen Prüfungstermin
    def set_exam_date_and_schedule(self, exam_date):
        self.exam_date = exam_date
        if self.student:
            self.student.create_and_add_exam_schedule(self.title, exam_date)

    # Setzt die Modulnote
    def set_grade(self, grade):
        self.grade = grade