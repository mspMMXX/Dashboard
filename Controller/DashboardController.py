from Model.Study import Study
import datetime as dt


class DashboardController:

    def __init__(self):
        self.study = Study(3, dt.date(2024, 1, 5))

    def get_modules(self):
        return self.study.modul_list.values()
