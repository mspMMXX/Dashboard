class AvgGrade:

    def __init__(self, db=None, student_id=None):
        """Initialisiert die AvgGrade-Klasse.
        Args:
            db: Die Datenbankverbindung.
            student_id: Die ID des Studenten.
        """
        self.db = db
        self.student_id = student_id
        self.planned_avg_grade = 0.0
        self.actual_avg_grade = 0.0
        self.actual_avg_grade_is_better_than_planned = None

    def calc_avg_grade(self, student_modul_dict):
        """Berechnet den tatsächlichen Notendurchschnitt basierend auf den Noten der Module.

        Args:
            student_modul_dict: Ein Dictionary mit den Modulen des Studenten.
        """
        sum_grade = 0.0
        sum_completed_moduls = 0.0
        for modul in student_modul_dict.values():
            print(f"Modul: {modul.title}, Note: {modul.grade}")  # Debugging-Ausgabe
            if modul.grade is not None:
                sum_grade += float(modul.grade)
                sum_completed_moduls += 1
        self.actual_avg_grade = sum_grade / sum_completed_moduls if sum_completed_moduls > 0 else None

    def calc_avg_grade_is_better_than_planned(self):
        """Bestimmt, ob der tatsächliche Notendurchschnitt besser als der geplante ist."""
        if self.actual_avg_grade is None or self.planned_avg_grade is None:
            self.actual_avg_grade_is_better_than_planned = None
        elif self.actual_avg_grade <= self.planned_avg_grade:
            self.actual_avg_grade_is_better_than_planned = True
        else:
            self.actual_avg_grade_is_better_than_planned = False

    def set_planned_avg_grade(self, planned_avg_grade):
        """Setzt den geplanten Notendurchschnitt.

        Args:
            planned_avg_grade: Der geplante Notendurchschnitt.
        """
        if 0.0 <= planned_avg_grade <= 5.0:
            self.planned_avg_grade = planned_avg_grade

    def save(self):
        """Speichert die geplanten und tatsächlichen Noten in der Datenbank."""
        self.calc_avg_grade_is_better_than_planned()

        query = "SELECT id FROM AvgGrade WHERE student_id = %s"
        params = (self.student_id,)
        result = self.db.fetch_one(query, params)

        if result:
            query = """
            UPDATE AvgGrade
            SET planned_avg_grade = %s, actual_avg_grade = %s, actual_avg_grade_is_better_than_planned = %s
            WHERE student_id = %s
            """
            params = (
                self.planned_avg_grade,
                self.actual_avg_grade,
                1 if self.actual_avg_grade_is_better_than_planned else 0,  # Speichert den booleschen Wert als 1 oder 0
                self.student_id
            )
        else:
            query = """
            INSERT INTO AvgGrade (planned_avg_grade, actual_avg_grade, actual_avg_grade_is_better_than_planned, student_id)
            VALUES (%s, %s, %s, %s)
            """
            params = (
                self.planned_avg_grade,
                self.actual_avg_grade,
                1 if self.actual_avg_grade_is_better_than_planned else 0,  # Speichert den booleschen Wert als 1 oder 0
                self.student_id
            )

        self.db.execute_query(query, params)  # Führt die Abfrage in der Datenbank aus

    def load(self):
        """Lädt die geplanten und tatsächlichen Noten aus der Datenbank."""
        query = "SELECT * FROM AvgGrade WHERE student_id = %s"
        params = (self.student_id,)
        result = self.db.fetch_one(query, params)

        print(f"Query result for student_id {self.student_id}: {result}")  # Debugging-Ausgabe

        if result:
            self.planned_avg_grade = result['planned_avg_grade']
            self.actual_avg_grade = result['actual_avg_grade']
            self.actual_avg_grade_is_better_than_planned = bool(result['actual_avg_grade_is_better_than_planned'])
        else:
            self.planned_avg_grade = 0.0
            self.actual_avg_grade = 0.0
            self.actual_avg_grade_is_better_than_planned = None

        print(f"Loaded AvgGrade: {self}")  # Debugging-Ausgabe

    def __repr__(self):
        """Gibt eine string-Repräsentation des AvgGrade-Objekts zurück."""
        return (f"AvgGrade(planned_avg_grade={self.planned_avg_grade}, actual_avg_grade={self.actual_avg_grade}, "
                f"actual_avg_grade_is_better_than_planned={self.actual_avg_grade_is_better_than_planned})")