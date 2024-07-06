from datetime import datetime, timedelta


class Modul:
    """
    Eine Klasse, die ein Studienmodul darstellt.
    """

    def __init__(self, db, modul_id, acronym, title, exam_format, image_path, status, student_id):
        """
        Initialisiert ein Modul-Objekt.
        Args:
            db: Die Datenbankverbindung.
            modul_id: Die ID des Moduls.
            acronym: Das Akronym des Moduls.
            title: Der Titel des Moduls.
            exam_format: Das Prüfungsformat des Moduls.
            image_path: Der Pfad zum Bild des Moduls.
            status: Der Status des Moduls.
            student_id: Die ID des Studenten, zu dem das Modul gehört.
        """
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

    def set_status(self, status):
        """
        Setzt den Status des Moduls und aktualisiert das Start- und Enddatum entsprechend.
        Args:
            status: Der neue Status des Moduls.
        """
        self.status = status
        self.set_start_date()
        self.set_end_date()
        self.save()

    def set_start_date(self):
        """
        Setzt das Startdatum des Moduls basierend auf dem Status "In Bearbeitung".
        """
        if self.status == "In Bearbeitung":
            if self.start_date is None:
                self.start_date = datetime.now()

    def set_end_date(self):
        """
        Setzt das Enddatum des Moduls basierend auf dem Status "Abgeschlossen".
        """
        if self.status == "Abgeschlossen":
            if self.end_date is None:
                self.end_date = datetime.now()

    def set_deadline(self, student):
        """
        Generiert die Deadline für den Abschluss des Moduls basierend auf der Studiendauer des Studenten.
        Args:
            student: Das Studenten-Objekt, das die Studiendauer enthält.
        """
        time_for_modul = student.study.study_duration * 365 / 36
        if self.start_date:
            self.deadline = self.start_date + timedelta(days=time_for_modul)
        else:
            self.deadline = None

    def set_exam_date_and_schedule(self, exam_date, student):
        """
        Setzt das Prüfungsdatum und erstellt einen Prüfungstermin.
        Args:
            exam_date: Das Datum der Prüfung.
            student: Das Studenten-Objekt, das den Termin erstellen soll.
        """
        self.exam_date = exam_date
        student.create_and_add_exam_schedule(self.title, exam_date)
        self.save()

    def set_grade(self, grade):
        """
        Setzt die Note des Moduls und speichert das Modul.
        Args:
            grade: Die Note des Moduls.
        """
        self.grade = grade
        self.save()

    def save(self):
        """
        Speichert das Modul in der Datenbank.
        Wenn das Modul bereits existiert, wird es aktualisiert. Andernfalls wird ein neues Modul erstellt.
        """
        query = "SELECT id FROM Modul WHERE modul_id = %s AND student_id = %s"
        params = (self.modul_id, self.student_id)
        result = self.db.fetch_one(query, params)

        if result:
            self.id = result['id']
            query = """
             UPDATE Modul
             SET acronym = %s, title = %s, exam_format = %s, image_path = %s, status = %s, 
                 start_date = %s, end_date = %s, deadline = %s, exam_date = %s, grade = %s, student_id = %s
             WHERE id = %s
             """
            params = (self.acronym, self.title, self.exam_format, self.image_path, self.status,
                      self.start_date, self.end_date, self.deadline, self.exam_date, self.grade, self.student_id,
                      self.id)
            self.db.execute_query(query, params)
        else:
            query = """
             INSERT INTO Modul (modul_id, acronym, title, exam_format, image_path, status, start_date, end_date, 
             deadline, exam_date, grade, student_id)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
             """
            params = (self.modul_id, self.acronym, self.title, self.exam_format, self.image_path, self.status,
                      self.start_date, self.end_date, self.deadline, self.exam_date, self.grade, self.student_id)
            self.db.execute_query(query, params)
            self.id = self.db.cursor.lastrowid

    def load(self, modul_id):
        """
        Lädt die Modul-Daten aus der Datenbank basierend auf der Modul-ID.

        Args:
            modul_id: Die ID des zu ladenden Moduls.
        """
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
