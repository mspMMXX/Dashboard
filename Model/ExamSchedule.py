from Model.Schedule import Schedule


# Kind von Schedule
class ExamSchedule(Schedule):

    def __init__(self, db, schedule_title, schedule_date, student_id, exam_schedule_color=None):
        super().__init__(db, schedule_title, schedule_date, student_id)
        if exam_schedule_color is None:
            self.exam_schedule_color = "red"
        else:
            self.exam_schedule_color = exam_schedule_color
