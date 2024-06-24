from Study import Study
from AvgGrades import AvgGrades
from Schedule import Schedule
from ExamSchedule import ExamSchedule


class Student:

    def __init__(self, last_name, first_name, student_number, study_duration, study_start_date, planned_avg_grade):
        self.last_name = last_name
        self.first_name = first_name
        self.student_number = student_number
        self.study = Study(study_duration, study_start_date)
        self.student_moduls = self.study.modul_list
        self.avg_grades = AvgGrades(planned_avg_grade)
        self.schedule_list = []

    def remove_schedule(self, schedule_id):
        for schedul in self.schedule_list:
            if schedul.schedule_id == schedule_id:
                self.schedule_list.remove(schedul)

    def create_and_add_schedule(self, schedule_title, schedule_date):
        schedule = Schedule(schedule_title, schedule_date)
        self.schedule_list.append(schedule)

    def create_and_add_exam_schedule(self, exam_schedule_title, exam_schedule_date):
        exam_schedule = ExamSchedule(exam_schedule_title, exam_schedule_date)
        self.schedule_list.append(exam_schedule)
