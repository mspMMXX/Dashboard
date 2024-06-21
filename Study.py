import datetime as dt
from Modul import Modul


def initialize_moduls():
    module = [
        Modul(1, "Test1", "Java", "Klausur", "Bild1"),
        Modul(2, "Test2", "Python", "Portfolio", "Bild2"),
        Modul(2, "Test3", "Swift", "Projektbericht", "Bild3")
    ]
    return module


class Study:

    COURSE_OF_STUDY = "Softwareentwicklung"

    def __init__(self, study_duration, study_start_date):
        self.study_duration = study_duration
        self.study_start_date = study_start_date
        self.graduation_date = self.set_graduation_date()
        self.calculated_graduation_date = self.set_calculated_graduation_date()
        self.calculated_graduation_date_color = self.set_calculated_graduation_date_color()
        self.modul_list = initialize_moduls()

    def set_graduation_date(self):
        return self.study_start_date.replace(year=self.study_start_date + self.study_duration)

    def set_study_start_date(self, study_start_date):
        self.study_start_date = study_start_date
        if self.study_duration is not None:
            self.graduation_date = self.study_start_date.replace(year=self.study_start_date + self.study_duration)

    def set_calculated_graduation_date(self):
        sum_modul_time = 0
        sum_completed_moduls = 0
        for modul in self.modul_list:
            if modul.status is "Abgeschlossen":
                modul_time = (modul.end_date - modul.start_date).days
                sum_modul_time += modul_time
                sum_completed_moduls += 1
        if sum_completed_moduls > 0:
            avg_days_to_complete = (sum_modul_time / sum_completed_moduls) * 36
            return self.study_start_date + dt.timedelta(days=self.study_start_date + avg_days_to_complete)
        else:
            return "Noch kein Modul abgeschlossen"

    def set_calculated_graduation_date_color(self):
        if self.graduation_date >= self.set_calculated_graduation_date():
            return True
        else:
            return False
