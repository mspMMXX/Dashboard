from Model.Study import Study
from Model.Student import Student
from Model.IUInformation import IUInformation
from DB.DataBase import DataBase
import datetime as dt


class DashboardController:

    def __init__(self):
        db = DataBase(host="localhost", user="root", password="", database="iu_dashboard")
        self.study = Study(3, dt.date(2024, 1, 5))
        self.student = Student(db, 3, dt.date(2024, 1, 5),  "Mustermann", "Max", 3249823)
        self.iu_info = IUInformation()

    # Gibt das Modul-Dictionary zurück.
    def get_modules(self):
        return list(self.study.modul_list.values())

    # Erstellt einen neuen Termin und fügt ihn zu schedule_list hinzu.
    def create_new_schedule(self, title, date):
        self.student.create_and_add_schedule(title, date)

    # Löscht den Termin aus schedule_list.
    def delete_schedule(self, schedule_id):
        self.student.remove_schedule(schedule_id)

    # Gibt die schedule_list zurück.
    def get_schedules(self):
        return self.student.schedule_list

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
