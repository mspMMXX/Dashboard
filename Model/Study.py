import datetime as dt
from Model.Modul import Modul


class Study:

    COURSE_OF_STUDY = "Softwareentwicklung"

    def __init__(self, db, study_duration, study_start_date, student_id):
        self.db = db
        self.study_duration = study_duration
        self.study_start_date = study_start_date
        self.student_id = student_id
        self.modul_list = {}
        self.load_moduls_from_db()
        self.graduation_date = self.calc_graduation_date()
        self.expected_graduation_date = self.graduation_date
        self.expected_graduation_date_is_before_graduation_date = True

    def load_moduls_from_db(self):
        query = "SELECT * FROM Modul WHERE student_id = %s"
        params = (self.student_id,)
        result = self.db.fetch_all(query, params)

        if result:
            for modul_data in result:
                modul = Modul(self.db, modul_data['modul_id'], modul_data['acronym'], modul_data['title'],
                              modul_data['exam_format'], modul_data['image_path'], modul_data['status'],
                              modul_data['student_id'])
                modul.id = modul_data['id']
                modul.start_date = modul_data['start_date']
                modul.end_date = modul_data['end_date']
                modul.deadline = modul_data['deadline']
                modul.exam_date = modul_data['exam_date']
                modul.grade = modul_data['grade']
                self.modul_list[modul.modul_id] = modul
        else:
            self.initialize_moduls()
            self.save_initial_moduls()

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
            1: Modul(self.db, 1, "DLBDSIDS01_D", "Einführung in Data Science", "Fachpräsentation",
                     "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                     "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            2: Modul(self.db, 2, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                     "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                     "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            3: Modul(self.db, 3, "DLBDSIDS01_D", "Einführung in Data Science", "Fachpräsentation",
                     "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                     "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            4: Modul(self.db, 4, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                     "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                     "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            5: Modul(self.db, 5, "DLBDSIDS01_D", "Einführung in Data Science", "Fachpräsentation",
                     "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                     "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            6: Modul(self.db, 6, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                     "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                     "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            7: Modul(self.db, 7, "DLBDSIDS01_D", "Einführung in Data Science", "Fachpräsentation",
                     "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                     "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            8: Modul(self.db, 8, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                     "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                     "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            9: Modul(self.db, 9, "DLBDSIDS01_D", "Einführung in Data Science", "Fachpräsentation",
                     "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                     "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            10: Modul(self.db, 10, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            11: Modul(self.db, 11, "DLBDSIDS01_D", "Einführung in Data Science", "Fachpräsentation",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            12: Modul(self.db, 12, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            13: Modul(self.db, 13, "DLBDSIDS01_D", "Einführung in Data Science", "Fachpräsentation",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            14: Modul(self.db, 14, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            15: Modul(self.db, 15, "DLBDSIDS01_D", "Einführung in Data Science", "Fachpräsentation",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            16: Modul(self.db, 16, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            17: Modul(self.db, 17, "DLBDSIDS01_D", "Einführung in Data Science", "Fachpräsentation",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            18: Modul(self.db, 18, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            19: Modul(self.db, 19, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            20: Modul(self.db, 20, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            21: Modul(self.db, 21, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            22: Modul(self.db, 22, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            23: Modul(self.db, 23, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            24: Modul(self.db, 24, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            25: Modul(self.db, 25, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            26: Modul(self.db, 26, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            27: Modul(self.db, 27, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            28: Modul(self.db, 28, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            29: Modul(self.db, 29, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            30: Modul(self.db, 30, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            31: Modul(self.db, 31, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            32: Modul(self.db, 32, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            33: Modul(self.db, 33, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            34: Modul(self.db, 34, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            35: Modul(self.db, 35, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
            36: Modul(self.db, 36, "DLBDSIDS02_D", "Einführung in Data", "Klausur",
                      "/Users/msp/Dropbox/07_IU/11_Objektorientierte_Programmierung_Python/02_Portfolio/01_Code/"
                      "Dashboard/Images/Data_Science.png", "Offen", self.student_id),
        }

    def save_initial_moduls(self):  # Neue Methode zum Speichern der initialisierten Module in der Datenbank
        for modul in self.modul_list.values():
            modul.save()
