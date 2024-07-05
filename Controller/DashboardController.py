# Datei: Controller/DashboardController.py
from Model.Study import Study
from Model.Student import Student
from Model.IUInformation import IUInformation
from DB.DataBase import DataBase
from datetime import datetime
from Model.Schedule import Schedule
import datetime as dt


class DashboardController:

    def __init__(self):
        self.db = DataBase(host="localhost", user="root", password="", database="iu_dashboard")
        self.student = self.load_student()
        self.study = Study(self.db, 3, dt.date(2024, 1, 5), self.student.id)
        self.iu_info = IUInformation()
        self.modules = self.study.modul_list.values()
        self.load_schedules()

    def load_student(self):
        query = "SELECT * FROM Student LIMIT 1"
        student_data = self.db.fetch_one(query, None)
        if student_data:
            student = Student(self.db, student_data['study_duration'], student_data['study_start_date'],
                              student_data['last_name'], student_data['first_name'], student_data['student_number'])
            student.id = student_data['id']
            return student
        else:
            student = Student(self.db, 3, dt.date(2024, 1, 5), "Mustermann", "Max", 3249823)
            student.save()
            return student

    def load_schedules(self):
        schedules = self.get_schedules()
        for schedule_data in schedules:
            schedule = Schedule.from_dict(schedule_data)
            self.student.schedule_list.append(schedule)

    def get_schedules(self):
        try:
            query = "SELECT * FROM Schedule WHERE student_id = %s"
            params = (self.student.id,)
            return self.db.fetch_all(query, params)
        except Exception as e:
            print(f"Fehler beim Abrufen der Termine aus der Datenbank: {str(e)}")
            return []

    # Gibt das Modul-Dictionary zurück.
    def get_modules(self):
        return list(self.study.modul_list.values())

    # Erstellt einen neuen Termin und fügt ihn zu schedule_list hinzu.
    def create_new_schedule(self, title, date):
        try:
            exam_date = datetime.strptime(date, '%d.%m.%Y %H:%M')
            formatted_date = exam_date.strftime('%Y-%m-%d %H:%M:%S')

            query = "INSERT INTO Schedule (title, schedule_date, student_id) VALUES (%s, %s, %s)"
            params = (title, formatted_date, self.student.id)
            self.db.execute_query(query, params)

            print("Neuer Termin wurde erfolgreich in die Datenbank eingefügt.")
        except ValueError:
            print("Fehler beim Konvertieren des Datumsformats.")
        except Exception as e:
            print(f"Fehler beim Erstellen eines neuen Termins in der Datenbank: {str(e)}")

    # Löscht den Termin aus schedule_list.
    def delete_schedule(self, schedule_id):
        try:
            query = "DELETE FROM Schedule WHERE id = %s"
            params = (schedule_id,)
            self.db.execute_query(query, params)
            print(f"Termin mit ID {schedule_id} wurde erfolgreich gelöscht.")
        except Exception as e:
            print(f"Fehler beim Löschen eines Termins aus der Datenbank: {str(e)}")

    # Setzt den geplanten Notendurchschnitt.
    def set_planned_avg_grade(self, avg_grade):
        self.student.avg_grade.set_planned_avg_grade(float(avg_grade))

    # Gibt den geplanten Notendurchschnitt zurück.
    def get_planned_avg_grade(self):
        return self.student.avg_grade

    # Berechnet den tatsächlichen Notendurchschnitt.
    def calc_avg_grade(self):
        self.student.avg_grade.calc_avg_grade(self.study.modul_list)

    # Kontrolliert, ob der geplante Notendurchschnitt besser oder schlechter als der tatsächliche ist.
    def avg_is_better_than_planned(self):
        self.student.avg_grade.calc_avg_grade_is_better_than_planned()

    # Gibt den boolschen Wert von avg_is_bestter_than_planned
    def get_avg_is_better_than_planned(self):
        return self.student.avg_grade.actual_avg_grade_is_better_than_planned

    def set_exam_date_for_modul(self, modul_id, exam_date):
        modul = self.study.modul_list.get(modul_id)
        if modul:
            modul.set_exam_date_and_schedule(exam_date, self.student)
