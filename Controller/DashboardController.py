from Model.Study import Study
from Model.Student import Student
from Model.IUInformation import IUInformation
import datetime as dt


class DashboardController:

    def __init__(self):
        self.study = Study(3, dt.date(2024, 1, 5))
        self.student = Student("Mustermann", "Max", 12932823, 3)
        self.iu_info = IUInformation()

    def get_modules(self):
        return list(self.study.modul_list.values())

    def create_new_schedule(self, title, date):
        self.student.create_and_add_schedule(title, date)

    def delete_schedule(self, schedule_id):
        self.student.remove_schedule(schedule_id)

    def get_schedules(self):
        return self.student.schedule_list

    def set_planned_avg_grade(self, avg_grade):
        self.student.avg_grade.set_planned_avg_grade(float(avg_grade))

    def get_planned_avg_grade(self):
        return self.student.avg_grade

    def calc_avg_grade(self):
        print("Berechne den Notendurchschnitt...")
        self.student.avg_grade.calc_avg_grade(self.study.modul_list)

    def avg_is_better_than_planned(self):
        self.student.avg_grade.calc_avg_grade_is_better_than_planned()
