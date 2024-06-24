import datetime as dt
from Modul import Modul


class Study:

    COURSE_OF_STUDY = "Softwareentwicklung"

    def __init__(self, study_duration, study_start_date):
        self.study_duration = study_duration
        self.study_start_date = study_start_date
        self.graduation_date = self.set_graduation_date()
        self.calculated_graduation_date = self.calculate_graduationdate()
        self.modul_list = []
        self.initialize_moduls()
        self.calculated_graduation_date_is_before_graduation_date = (
            self.calculate_graduation_date_is_before_graduation_date())

    def set_graduation_date(self):
        return self.study_start_date.replace(year=self.study_start_date + self.study_duration)

    def set_study_start_date(self, study_start_date):
        self.study_start_date = study_start_date
        if self.study_duration is not None:
            self.graduation_date = self.study_start_date.replace(year=self.study_start_date + self.study_duration)

    # Methode zum errechnen des voraussichtlichen Abschlussdatums. Berechnet auf die durchschnittliche
    # Bearbeitungsdauer der Module
    def calculate_graduationdate(self):
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

    # Berechnet ob das voraussichtlich errechnete Abschlussdatum vor oder am selben Tag wie das Abschlussdatum ist
    def calculate_graduation_date_is_before_graduation_date(self):
        if self.graduation_date >= self.calculate_graduationdate():
            return True
        else:
            return False

    # Methode zur erstellung von Modulen. Diese werden dann gleich der Liste hinzugefügt
    def add_modul(self, modul_id, acronym, title, exam_format, image):
        modul = Modul(modul_id, acronym, title, exam_format, image)
        self.modul_list.append(modul)

    # Mit dieser Mehtode werden alle Module des Studiengangs Softwareentwicklung angelegt und im Konstruktor aufgerufen
    def initialize_moduls(self):
        self.add_modul(1, "Test", "Titel", "Klausur", "Bild")

