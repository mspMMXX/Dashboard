from Study import Study


def calculate_avg_grade(modul_list):
    sum_grade = 0
    sum_completed_moduls = 0
    for modul in Study.modul_list:
        if modul.grade is not None:
            sum_grade += modul.grade
            sum_completed_moduls += 1
    return sum_grade / sum_completed_moduls


class AvgGrades:

    actual_avg_grade = calculate_avg_grade()
    # actual_avg_grade_color = Color?

    def __init__(self, planned_avg_grade):
        self.planned_avg_grade = planned_avg_grade
