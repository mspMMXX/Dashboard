from Model.Study import Study
from Model.Student import Student
import datetime as dt


class DashboardController:

    def __init__(self):
        self.study = Study(3, dt.date(2024, 1, 5))

    def get_modules(self):
        return list(self.study.modul_list.values())

    def get_schedules(self):
        return Student.schedule_list
