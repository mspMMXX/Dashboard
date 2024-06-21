import datetime as dt


class Study:

    modul_list = []
    avg_duration_in_days = None

    def __init__(self):
        self.course_of_study = "Softwareentwicklung"
        self.study_duration = None
        self.study_start_date = None
        self.graduation_date = None
        self.calculated_graduation_date = None
        self.calculated_graduation_date_color = None

    def set_study_duration_and_graduation_date(self, study_duration):
        self.study_duration = study_duration
        if self.study_start_date is not None:
            self.graduation_date = self.study_start_date.replace(year=self.study_start_date + self.study_duration)

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
            self.calculated_graduation_date = self.study_start_date + dt.timedelta(days=self.study_start_date +
                                                                                   avg_days_to_complete)

    def calculate_graduation_date(self, study_start_date, modul_list):
        # Berechnen der voraussichtlichen Dauer
        # Anzahl der Module (36) * Die Summe der Bearbeitungszeiten (Tage) aller abgeschlossenen Modulen =
        # Durchschnittliche Tage bis zum Abschluss. Diese Tage zu dem Anfangsdatum hinzurechnen = Voraussichtliches
        # Abschlussdatum
        pass
