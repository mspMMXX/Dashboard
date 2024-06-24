from Student import Student

class AvgGrades:

    def __init__(self, planned_avg_grade):
        self.planned_avg_grade = planned_avg_grade
        self.actual_avg_grade = self.calculate_avg_grade()
        self.actual_avg_grade_is_better_than_planned = self.actual_avg_grade_is_better_than_planned()

    # Berechnet den Notendurchschnitt auf Basis der Menge an abgeschlossenen Module und Notensumme
    def calculate_avg_grade(self, student_modul_list):
        sum_grade = 0.0
        sum_completed_moduls = 0.0
        for modul in student_modul_list:
            if modul.grade is not None:
                sum_grade += modul.grade
                sum_completed_moduls += 1
        return sum_grade / sum_completed_moduls

    # Kontrolliert ob der Notendurchschnitt besser oder schlechter als der geplante ist
    def actual_avg_grade_is_better_than_planned(self, planned_avg_grade, actual_avg_grade):
        if actual_avg_grade <= planned_avg_grade:
            return True
        else:
            return False

