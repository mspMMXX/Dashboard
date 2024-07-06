from Model.Study import Study
from Model.Student import Student
from Model.IUInformation import IUInformation
from DB.DataBase import DataBase
from datetime import datetime
from Model.Schedule import Schedule
import datetime as dt


class DashboardController:

    def __init__(self):
        """Initialisiert den DashboardController und lädt die notwendigen Daten."""
        self.db = DataBase(host="localhost", user="root", password="", database="iu_dashboard")
        self.student = self.load_student()  # Lädt den Studentendatensatz
        self.study = Study(self.db, 3, dt.date(2024, 1, 5), self.student.id)  # Initialisiert das Study-Objekt
        self.study.load()  # Lädt die Studieninformationen
        self.iu_info = IUInformation()  # Lädt die IU-Informationen
        self.modules = self.study.modul_list.values()  # Lädt die Modulliste
        self.load_schedules()  # Lädt die Terminliste

    def get_schedules(self):
        """Gibt alle Termine des Studenten aus der Datenbank zurück."""
        try:
            query = "SELECT * FROM Schedule WHERE student_id = %s"
            params = (self.student.id,)
            return self.db.fetch_all(query, params)  # Führt die Datenbankabfrage aus
        except Exception as e:
            print(f"Fehler beim Abrufen der Termine aus der Datenbank: {str(e)}")
            return []

    def get_modules(self):
        """Gibt die Modulliste des Studenten zurück."""
        return list(self.study.modul_list.values())

    def create_new_schedule(self, title, date):
        """Erstellt einen neuen Termin und fügt ihn zur Terminliste hinzu."""
        try:
            exam_date = datetime.strptime(date, '%d.%m.%Y %H:%M')
            formatted_date = exam_date.strftime('%Y-%m-%d %H:%M:%S')

            query = "INSERT INTO Schedule (title, schedule_date, student_id) VALUES (%s, %s, %s)"
            params = (title, formatted_date, self.student.id)
            self.db.execute_query(query, params)  # Führt die Einfügeoperation in der Datenbank aus

        except ValueError:
            print("Fehler beim Konvertieren des Datumsformats.")
        except Exception as e:
            print(f"Fehler beim Erstellen eines neuen Termins in der Datenbank: {str(e)}")

    def set_planned_avg_grade(self, avg_grade):
        """Setzt den geplanten Notendurchschnitt des Studenten."""
        self.student.avg_grade.set_planned_avg_grade(avg_grade)
        self.student.save()  # Speichert die Studentendaten

    def calc_avg_grade(self):
        """Berechnet den tatsächlichen Notendurchschnitt des Studenten."""
        self.student.avg_grade.calc_avg_grade(self.study.modul_list)

    def avg_is_better_than_planned(self):
        """Kontrolliert, ob der geplante Notendurchschnitt besser oder schlechter als der tatsächliche Durchschnitt
        ist."""
        self.student.avg_grade.calc_avg_grade_is_better_than_planned()

    def get_avg_is_better_than_planned(self):
        """Gibt den booleschen Wert zurück, ob der tatsächliche Notendurchschnitt besser ist als der geplante
        Durchschnitt."""
        return self.student.avg_grade.actual_avg_grade_is_better_than_planned

    def save_student_data(self, planned_grade_entry):
        """Speichert die Studentendaten inklusive der geplanten Noten."""
        self.student.avg_grade.set_planned_avg_grade(float(planned_grade_entry.get()))  # Setzt die geplanten Noten
        self.student.avg_grade.calc_avg_grade_is_better_than_planned()  # Berechnet, ob der tatsächliche Durchschnitt
        # besser als der geplante ist
        self.student.save()  # Speichert die Studentendaten
        self.study.save()  # Speichert die Studiendaten

    def load_schedules(self):
        """Lädt alle Termine aus der Datenbank und fügt sie zur Studententerminliste hinzu."""
        schedules = self.get_schedules()
        for schedule_data in schedules:
            schedule = Schedule.from_dict(schedule_data)  # Erstellt Schedule-Objekte aus den Datenbankeinträgen
            self.student.schedule_list.append(schedule)  # Fügt die Termine zur Studententerminliste hinzu

    def load_student(self):
        """Lädt die Studentendatenbankeinträge inklusive der geplanten und aktuellen Noten."""
        query = "SELECT * FROM Student LIMIT 1"
        student_data = self.db.fetch_one(query, None)  # Abfrage der Studentendaten

        if student_data:
            # Erzeugt ein Student-Objekt mit den abgerufenen Daten
            student = Student(self.db, student_data['study_duration'], student_data['study_start_date'],
                              student_data['last_name'], student_data['first_name'], student_data['student_number'])
            student.id = student_data['id']
            student.avg_grade.student_id = student.id  # Setzt die student_id für AvgGrade
            student.avg_grade.load()  # Lädt die Noteninformation
            return student
        else:
            # Erstellt und speichert einen neuen Studentensatz, falls keiner vorhanden ist
            student = Student(self.db, 3, dt.date(2024, 1, 5), "Mustermann", "Max", 3249823)
            student.save()
            return student

    def delete_schedule(self, schedule_id):
        """Löscht einen Termin aus der Datenbank und der Terminliste des Studenten."""
        try:
            query = "DELETE FROM Schedule WHERE id = %s"
            params = (schedule_id,)
            self.db.execute_query(query, params)  # Führt die Löschoperation in der Datenbank aus
            print(f"Termin mit ID {schedule_id} wurde erfolgreich gelöscht.")
        except Exception as e:
            print(f"Fehler beim Löschen eines Termins aus der Datenbank: {str(e)}")

    def cleanup(self):
        """Schließt die Datenbankverbindung ordnungsgemäß.
        Diese Methode sollte aufgerufen werden, bevor die Anwendung geschlossen wird, um sicherzustellen,
        dass alle Datenbankressourcen freigegeben werden und keine offenen Verbindungen verbleiben.
        """
        self.db.close()
