from Model.Study import Study
from Model.Student import Student
import datetime as dt


class DashboardController:

    def __init__(self):
        self.study = Study(3, dt.date(2024, 1, 5))
        self.student = Student("Mustermann", "Max", 12932823, 3)

    def get_modules(self):
        return list(self.study.modul_list.values())

    def create_new_schedule(self, title, date):
        self.student.create_and_add_schedule(title, date)

    def delete_schedule(self, schedule_id):
        self.student.remove_schedule(schedule_id)

    def get_schedules(self):
        return self.student.schedule_list
