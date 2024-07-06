from Model.Schedule import Schedule


class ExamSchedule(Schedule):
    """
    Eine Klasse, die einen Klausurtermin (ExamSchedule) darstellt.
    Erbt von der Klasse Schedule.
    """

    def __init__(self, db, schedule_title, schedule_date, student_id, exam_schedule_color=None):
        """
        Initialisiert ein ExamSchedule-Objekt.
        Args:
            db: Die Datenbankverbindung.
            schedule_title: Der Titel des Klausurtermins.
            schedule_date: Das Datum und die Uhrzeit des Klausurtermins.
            student_id: Die ID des Studenten, zu dem der Termin gehört.
            exam_schedule_color: (Optional) die Farbe des Klausurtermins.
        """
        super().__init__(db, schedule_title, schedule_date, student_id)
        if exam_schedule_color is None:
            self.exam_schedule_color = "red"
        else:
            self.exam_schedule_color = exam_schedule_color
