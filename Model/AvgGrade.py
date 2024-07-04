class AvgGrade:

    def __init__(self):
        self.planned_avg_grade = 0.0
        self.actual_avg_grade = 0.0
        self.actual_avg_grade_is_better_than_planned = None

    # Berechnet den Notendurchschnitt auf Basis der Menge an Noten
    def calc_avg_grade(self, student_modul_dict):
        sum_grade = 0.0
        sum_completed_moduls = 0.0
        for modul in student_modul_dict.values():
            print(f"Modul: {modul.title}, Note: {modul.grade}")
            if modul.grade is not None:
                sum_grade += float(modul.grade)
                sum_completed_moduls += 1
        self.actual_avg_grade = sum_grade / sum_completed_moduls if sum_completed_moduls > 0 else None

    # Kontrolliert, ob der Notendurchschnitt besser oder schlechter als der geplante ist
    def calc_avg_grade_is_better_than_planned(self):
        if self.actual_avg_grade == 0.0 or self.planned_avg_grade is None:
            self.actual_avg_grade_is_better_than_planned = None
        elif self.actual_avg_grade <= self.planned_avg_grade:
            self.actual_avg_grade_is_better_than_planned = True
        else:
            self.actual_avg_grade_is_better_than_planned = False

    # Übergibt den geplanten Notendurchschnitt
    def set_planned_avg_grade(self, planned_avg_grade):
        if 0.0 <= planned_avg_grade <= 5.0:
            self.planned_avg_grade = planned_avg_grade
