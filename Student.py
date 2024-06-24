from Study import Study
from AvgGrades import AvgGrades


class Student:

    def __init__(self, last_name, first_name, student_number, study_duration, study_start_date):
        self.last_name = last_name
        self.first_name = first_name
        self.student_number = student_number
        self.study = self.initialize_study(study_duration, study_start_date)
        self.student_moduls = self.study.modul_list
        self.avg_grades = self.initialize_avg_grades()


    def initialize_study(self, study_duration, study_start_date):
        study = Study(study_duration, study_start_date)
        return study

    def initialize_avg_grades(self, planned_avg_grade):
        avg_grade = AvgGrades(planned_avg_grade)
        return avg_grade

