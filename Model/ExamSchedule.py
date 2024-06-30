from .Schedule import Schedule


# Kind von Schedule
class ExamSchedule(Schedule):

    def __init__(self, schedule_title, schedule_date, exam_schedule_color=None):
        super().__init__(schedule_title, schedule_date)
        if exam_schedule_color is None:
            self.exam_schedule_color = "red"
        else:
            self.exam_schedule_color = exam_schedule_color
