

# Berechnet den Notendurchschnitt auf Basis der Menge an abgeschlossenen Module und Notensumme
def calc_avg_grade(student_modul_list):
    sum_grade = 0.0
    sum_completed_moduls = 0.0
    for modul in student_modul_list:
        if modul.grade is not None:
            sum_grade += modul.grade
            sum_completed_moduls += 1
    return sum_grade / sum_completed_moduls


# Kontrolliert, ob der Notendurchschnitt besser oder schlechter als der geplante ist
def calc_avg_grade_is_better_than_planned(planned_avg_grade, actual_avg_grade):
    if actual_avg_grade <= planned_avg_grade:
        return True
    else:
        return False


class AvgGrade:

    def __init__(self, planned_avg_grade, student_moduls_list):
        self.planned_avg_grade = planned_avg_grade
        self.actual_avg_grade = calc_avg_grade(student_moduls_list)
        self.actual_avg_grade_is_better_than_planned = calc_avg_grade_is_better_than_planned(self.planned_avg_grade,
                                                                                             self.actual_avg_grade)
