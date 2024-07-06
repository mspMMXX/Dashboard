import datetime as dt
from Model.Schedule import Schedule
from Model.ExamSchedule import ExamSchedule


class Student:
    """
    Eine Klasse, die die Informationen eines Studenten verwaltet.
    Diese Klasse implementiert das Singleton-Muster, um sicherzustellen, dass es nur eine Instanz eines Studenten gibt.
    """
    _instance = None
    schedule_list = []

    def __new__(cls, *args, **kwargs):
        """
        Implementiert das Singleton-Muster.
        """
        if cls._instance is None:
            cls._instance = super(Student, cls).__new__(cls)
        return cls._instance

    def __init__(self, db, study_duration, study_start_date, last_name=None, first_name=None, student_number=None):
        """
        Initialisiert ein Student-Objekt.

        Args:
            db: Die Datenbankverbindung.
            study_duration: Die Studiendauer in Jahren.
            study_start_date: Das Datum des Studienbeginns.
            last_name: der Nachname des Studenten.
            first_name: Der Vorname des Studenten.
            student_number: Die Matrikelnummer des Studenten.
        """
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
            self.avg_grade = AvgGrade(self.db, self.id)
            self.schedule_list = []
            self.initialized = True

    def create_and_add_schedule(self, schedule_title, schedule_date):
        """
        Erstellt einen neuen Termin und fügt ihn zur Terminliste des Studenten hinzu.
        Args:
            schedule_title: Der Titel des Termins.
            schedule_date: Das Datum des Termins.
        """
        if isinstance(schedule_date, str):
            schedule_date = dt.datetime.strptime(schedule_date, "%d.%m.%Y %H:%M")
        schedule = Schedule(self.db, schedule_title, schedule_date, self.id)
        self.schedule_list.append(schedule)
        schedule.save()

    def create_and_add_exam_schedule(self, exam_schedule_title, exam_schedule_date):
        """
        Erstellt einen neuen Klausurtermin und fügt ihn zur Terminliste des Studenten hinzu.
        Args:
            exam_schedule_title: Der Titel des Klausurtermins.
            exam_schedule_date: Das Datum des Klausurtermins.
        """
        if isinstance(exam_schedule_date, str):
            exam_schedule_date = dt.datetime.strptime(exam_schedule_date, "%d.%m.%Y %H:%M")
        exam_schedule = ExamSchedule(self.db, exam_schedule_title, exam_schedule_date, self.id)
        self.schedule_list.append(exam_schedule)
        exam_schedule.save()

    def save(self):
        """
        Speichert die Studenteninformationen in der Datenbank.
        Wenn der Student bereits existiert, wird er aktualisiert. Andernfalls wird ein neuer Eintrag erstellt.
        """
        query = "SELECT id FROM Student WHERE student_number = %s"
        params = (self.student_number,)
        result = self.db.fetch_one(query, params)

        if result:
            self.id = result['id']
            query = """
            UPDATE Student
            SET study_duration = %s, study_start_date = %s, last_name = %s, first_name = %s
            WHERE id = %s
            """
            params = (self.study_duration, self.study_start_date, self.last_name, self.first_name, self.id)
            self.db.execute_query(query, params)
        else:
            query = """
            INSERT INTO Student (study_duration, study_start_date, last_name, first_name, student_number)
            VALUES (%s, %s, %s, %s, %s)
            """
            params = (self.study_duration, self.study_start_date, self.last_name, self.first_name, self.student_number)
            self.db.execute_query(query, params)
            self.id = self.db.cursor.lastrowid

        self.avg_grade.student_id = self.id
        self.avg_grade.save()

    def load(self):
        """
        Lädt die Studenteninformationen aus der Datenbank basierend auf der Matrikelnummer.
        """
        query = "SELECT * FROM Student WHERE student_number = %s"
        params = (self.student_number,)
        result = self.db.fetch_one(query, params)

        if result:
            self.id = result['id']
            self.study_duration = result['study_duration']
            self.study_start_date = result['study_start_date']
            self.last_name = result['last_name']
            self.first_name = result['first_name']
            self.avg_grade.student_id = self.id  # Sicherstellen, dass student_id korrekt gesetzt ist
            self.avg_grade.load()  # Noten laden
