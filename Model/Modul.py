from datetime import datetime, timedelta


class Modul:
    def __init__(self, db, modul_id, acronym, title, exam_format, image_path, status, student_id):
        self.db = db
        self.modul_id = modul_id
        self.acronym = acronym
        self.title = title
        self.exam_format = exam_format
        self.image_path = image_path
        self.status = status
        self.start_date = None
        self.end_date = None
        self.deadline = None
        self.exam_date = None
        self.grade = None
        self.student_id = student_id
        self.id = None

    def save(self):
        if self.id is None:
            query = """
            INSERT INTO Modul (modul_id, acronym, title, exam_format, image_path, status, start_date, end_date, 
            deadline, exam_date, grade, student_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            params = (self.modul_id, self.acronym, self.title, self.exam_format, self.image_path, self.status,
                      self.start_date, self.end_date, self.deadline, self.exam_date, self.grade, self.student_id)
            self.db.execute_query(query, params)
            self.id = self.db.cursor.lastrowid
        else:
            query = """
            UPDATE Modul
            SET modul_id = %s, acronym = %s, title = %s, exam_format = %s, image_path = %s, status = %s, 
            start_date = %s, end_date = %s, deadline = %s, exam_date = %s, grade = %s
            WHERE id = %s
            """
            params = (self.modul_id, self.acronym, self.title, self.exam_format, self.image_path, self.status,
                      self.start_date, self.end_date, self.deadline, self.exam_date, self.grade, self.id)
            self.db.execute_query(query, params)

    def load(self, modul_id):
        query = "SELECT * FROM Modul WHERE id = %s"
        params = (modul_id,)
        result = self.db.fetch_one(query, params)
        if result:
            self.id = result['id']
            self.modul_id = result['modul_id']
            self.acronym = result['acronym']
            self.title = result['title']
            self.exam_format = result['exam_format']
            self.image_path = result['image_path']
            self.status = result['status']
            self.start_date = result['start_date']
            self.end_date = result['end_date']
            self.deadline = result['deadline']
            self.exam_date = result['exam_date']
            self.grade = result['grade']
            self.student_id = result['student_id']

    def delete(self):
        if self.id:
            query = "DELETE FROM Modul WHERE id = %s"
            params = (self.id,)
            self.db.execute_query(query, params)
            self.id = None

    # Setzt den Status und das Start- und Abschlussdatum eines Moduls
    def set_status(self, status):
        self.status = status
        self.set_start_date()
        self.set_end_date()

    # Setzt das Startdatum basierend auf dem Status "In Bearbeitung"
    def set_start_date(self):
        if self.status == "In Bearbeitung":
            if self.start_date is None:  # Nur setzen, wenn es noch nicht gesetzt ist
                self.start_date = datetime.now()

    # Setzt das Enddatum basierend auf dem Status "Abgeschlossen"
    def set_end_date(self):
        if self.status == "Abgeschlossen":
            if self.end_date is None:  # Nur setzen, wenn es noch nicht gesetzt ist
                self.end_date = datetime.now()

    # Generiert die Deadline bis wann das Modul abgeschlossen werden muss
    def set_deadline(self, student):
        time_for_modul = student.study.study_duration * 365 / 36
        if self.start_date:
            self.deadline = self.start_date + timedelta(days=time_for_modul)
        else:
            self.deadline = None

    # Setzt das Prüfungsdatum und erstellt einen Prüfungstermin
    def set_exam_date_and_schedule(self, exam_date, student):
        self.exam_date = exam_date
        student.create_and_add_exam_schedule(self.title, exam_date)
        self.save()

    # Setzt die Modulnote
    def set_grade(self, grade):
        self.grade = grade
