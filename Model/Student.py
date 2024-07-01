# Singelton Klasse, da nur eine Instanz existieren soll und in anderen Klassen auf die seleben Attributwerte
# zugegriffen werden kann.
class Student:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Student, cls).__new__(cls)
        return cls._instance

    def __init__(self, last_name=None, first_name=None, student_number=None, study_duration=None,
                 study_start_date=None, planned_avg_grade=None):
        if not hasattr(self, "initialized"):
            from Model.Study import Study
            from Model.AvgGrade import AvgGrade
            self.last_name = last_name
            self.first_name = first_name
            self.student_number = student_number
            self.study = Study(study_duration, study_start_date)
            self.student_moduls = self.study.modul_list
            self.avg_grade = AvgGrade(planned_avg_grade, self.student_moduls)
            self.schedule_list = []
            self.initialized = True

    # Aktualisiert die Werte des Moduls
    def update_modul(self, modul_id, status=None, end_date=None, exam_date=None, grade=None):
        self.student_moduls[modul_id].acronym = status
        self.student_moduls[modul_id].end_date = end_date
        self.student_moduls[modul_id].exam_date = exam_date
        self.student_moduls[modul_id].grade = grade

    # Erstellt ein Termin und fügt ihn zur Liste hinzu
    def create_and_add_schedule(self, schedule_title, schedule_date):
        from Model.Schedule import Schedule
        schedule = Schedule(schedule_title, schedule_date)
        self.schedule_list.append(schedule)

    # Erstellt ein Klasusurtermin und fügt ihn zur Liste hinzu
    def create_and_add_exam_schedule(self, exam_schedule_title, exam_schedule_date):
        from Model.ExamSchedule import ExamSchedule
        exam_schedule = ExamSchedule(exam_schedule_title, exam_schedule_date, None)
        self.schedule_list.append(exam_schedule)

    # Löscht einen Termin
    def remove_schedule(self, schedule_id):
        for schedul in self.schedule_list:
            if schedul.schedule_id == schedule_id:
                self.schedule_list.remove(schedul)
