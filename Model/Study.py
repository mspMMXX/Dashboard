import datetime as dt
from Model.Modul import Modul


class Study:

    COURSE_OF_STUDY = "Softwareentwicklung"

    def __init__(self, study_duration, study_start_date):
        self.study_duration = study_duration
        self.study_start_date = study_start_date
        self.modul_list = {}
        self.initialize_moduls()
        self.graduation_date = self.calc_graduation_date()
        self.expected_graduation_date = self.graduation_date
        self.expected_graduation_date_is_before_graduation_date = True

    # Berechnet das Abschlussdatum basierend auf das Startdatum und der Studiendauer
    def calc_graduation_date(self):
        if self.study_start_date is None or self.study_duration is None:
            raise ValueError("study_start_date and study_duration must not be None")
        return self.study_start_date + dt.timedelta(days=self.study_duration * 365)

    # Methode zur Berechnung des voraussichtlichen Abschlussdatums. Basis der durchschnittlichen Bearbeitung der Module
    def calc_expected_graduation_date(self):
        sum_modul_time = 0
        sum_completed_moduls = 0
        for modul in self.modul_list.values():
            if modul.status == "Abgeschlossen":
                if modul.start_date is not None and modul.end_date is not None:
                    modul_time = (modul.end_date - modul.start_date).days
                    sum_modul_time += modul_time
                    sum_completed_moduls += 1
        if sum_completed_moduls > 0:
            avg_days_to_complete = (sum_modul_time / sum_completed_moduls) * 36
            self.expected_graduation_date = self.study_start_date + dt.timedelta(days=avg_days_to_complete)
        else:
            self.expected_graduation_date = self.graduation_date
        return self.expected_graduation_date

    # Berechnet, ob das voraussichtlich errechnete Abschlussdatum vor oder am selben Tag wie das Abschlussdatum ist
    def calc_expected_is_before_graduation_date(self):
        if self.graduation_date >= self.expected_graduation_date:
            self.expected_graduation_date_is_before_graduation_date = True
        else:
            self.expected_graduation_date_is_before_graduation_date = False

    # Anlegen aller Module des Studiengangs Softwareentwicklung
    def initialize_moduls(self):
        self.modul_list = {
            1: Modul(1, "DLBDSIDS01_D", "Einführung in Data Science",
                     "Fachpräsentation", image_path="/Users/msp/Dropbox/07_IU/"
                                                    "11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                                                    "Dashboard/Images/Data_Science.png", status="Offen"),
            2: Modul(2, "DLBDSIDS02_D", "Einführung in Data",
                     "Klausur",
                     image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            3: Modul(3, "DLBDSIDS01_D", "Einführung in Data Science",
                     "Fachpräsentation", image_path="/Users/msp/Dropbox/07_IU/"
                                                    "11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                                                    "Dashboard/Images/Data_Science.png", status="Offen"),
            4: Modul(4, "DLBDSIDS02_D", "Einführung in Data",
                     "Klausur",
                     image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            5: Modul(5, "DLBDSIDS01_D", "Einführung in Data Science",
                     "Fachpräsentation", image_path="/Users/msp/Dropbox/07_IU/"
                                                    "11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                                                    "Dashboard/Images/Data_Science.png", status="Offen"),
            6: Modul(6, "DLBDSIDS02_D", "Einführung in Data",
                     "Klausur",
                     image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            7: Modul(7, "DLBDSIDS01_D", "Einführung in Data Science",
                     "Fachpräsentation", image_path="/Users/msp/Dropbox/07_IU/"
                                                    "11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                                                    "Dashboard/Images/Data_Science.png", status="Offen"),
            8: Modul(8, "DLBDSIDS02_D", "Einführung in Data",
                     "Klausur",
                     image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            9: Modul(9, "DLBDSIDS01_D", "Einführung in Data Science",
                     "Fachpräsentation", image_path="/Users/msp/Dropbox/07_IU/"
                                                    "11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                                                    "Dashboard/Images/Data_Science.png", status="Offen"),
            10: Modul(10, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            11: Modul(11, "DLBDSIDS01_D", "Einführung in Data Science", "Fachpräsentation",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            12: Modul(12, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            13: Modul(13, "DLBDSIDS01_D", "Einführung in Data Science", "Fachpräsentation",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            14: Modul(14, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            15: Modul(1, "DLBDSIDS01_D", "Einführung in Data Science", "Fachpräsentation",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            16: Modul(16, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            17: Modul(17, "DLBDSIDS01_D", "Einführung in Data Science", "Fachpräsentation",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            18: Modul(18, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            19: Modul(19, "DLBDSIDS01_D", "Einführung in Data Science", "Fachpräsentation",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            20: Modul(20, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            21: Modul(21, "DLBDSIDS01_D", "Einführung in Data Science", "Fachpräsentation",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            22: Modul(22, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            23: Modul(23, "DLBDSIDS01_D", "Einführung in Data Science", "Fachpräsentation",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            24: Modul(24, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            25: Modul(25, "DLBDSIDS01_D", "Einführung in Data Science", "Fachpräsentation",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            26: Modul(26, "DLBDSIDS02_D", "Einführung in Data",
                      "Klausur",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            27: Modul(27, "DLBDSIDS01_D", "Einführung in Data Science",
                      "Fachpräsentation", image_path="/Users/msp/Dropbox/07_IU/"
                                                     "11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                                                     "Dashboard/Images/Data_Science.png", status="Offen"),
            28: Modul(28, "DLBDSIDS02_D", "Einführung in Data",
                      "Klausur",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            29: Modul(29, "DLBDSIDS01_D", "Einführung in Data Science",
                      "Fachpräsentation", image_path="/Users/msp/Dropbox/07_IU/"
                                                     "11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                                                     "Dashboard/Images/Data_Science.png", status="Offen"),
            30: Modul(30, "DLBDSIDS02_D", "Einführung in Data",
                      "Klausur",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            31: Modul(31, "DLBDSIDS01_D", "Einführung in Data Science",
                      "Fachpräsentation", image_path="/Users/msp/Dropbox/07_IU/"
                                                     "11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                                                     "Dashboard/Images/Data_Science.png", status="Offen"),
            32: Modul(32, "DLBDSIDS02_D", "Einführung in Data",
                      "Klausur",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            33: Modul(33, "DLBDSIDS01_D", "Einführung in Data Science",
                      "Fachpräsentation", image_path="/Users/msp/Dropbox/07_IU/"
                                                     "11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                                                     "Dashboard/Images/Data_Science.png", status="Offen"),
            34: Modul(34, "DLBDSIDS02_D", "Einführung in Data",
                      "Klausur",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen"),
            35: Modul(35, "DLBDSIDS01_D", "Einführung in Data Science",
                      "Fachpräsentation", image_path="/Users/msp/Dropbox/07_IU/"
                                                     "11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                                                     "Dashboard/Images/Data_Science.png", status="Offen"),
            36: Modul(36, "DLBDSIDS02_D", "Einführung in Data",
                      "Klausur",
                      image_path="/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/"
                                 "01_Code/Dashboard/Images/Data_Science.png", status="Offen")

        }
