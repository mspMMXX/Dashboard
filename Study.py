import datetime as dt
from Modul import Modul


class Study:

    COURSE_OF_STUDY = "Softwareentwicklung"

    def __init__(self, study_duration, study_start_date):
        self.study_duration = study_duration
        self.study_start_date = study_start_date
        self.graduation_date = self.calc_graduation_date()
        self.expected_graduation_date = self.calc_expected_graduation_date()
        self.expected_graduation_date_is_before_graduation_date = (
            self.calc_expected_is_before_graduation_date())
        self.modul_list = {}
        self.initialize_moduls()

    # Berechnet das Abschlussdatum basierend auf das Startdatum und der Studiendauer
    def calc_graduation_date(self):
        return self.study_start_date.replace(year=self.study_start_date + self.study_duration)

    # Methode zur Berechnung des voraussichtlichen Abschlussdatums. Basis der durchschnittlichen Bearbeitung der Module
    def calc_expected_graduation_date(self):
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

    # Berechnet, ob das voraussichtlich errechnete Abschlussdatum vor oder am selben Tag wie das Abschlussdatum ist
    def calc_expected_is_before_graduation_date(self):
        if self.graduation_date >= self.expected_graduation_date():
            return True
        else:
            return False

    # Anlegen aller Module des Studiengangs Softwareentwicklung
    def initialize_moduls(self):
        self.modul_list = {
            1: Modul(1, "BLABLA", "Titel", "Klausur", "image")
        }
