

class Modul:

    def __init__(self, modul_id, acronym, title, exam_format, image):
        self.modul_id = modul_id
        self.acronym = acronym
        self.title = title
        self.exam_format = exam_format
        self.image = image
        self.status = "Offen"
        self.start_date = None
        self.end_date = None
        self.deadline = None
        self.exam_date = None
        self.grade = None

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def set_deadline(self, deadline):
        self.deadline = deadline

    def set_exam_date(self, exam_date):
        self.exam_date = exam_date

    def set_grade(self, grade):
        self.grade = grade

    def set_status(self, status):
        self.status = status

    def __str__(self):
        return f"{self.acronym}, {self.title}, {self.exam_format}, {self.image}, {self.status}, {self.start_date}, {self.end_date}, {self.deadline}, {self.exam_date}, {self.grade}"

    def calculate_deadline(self):
        pass


modul1 = Modul("DIELSDK_1", "Python", "Klausur", "Image", "In Bearbeitung")
print(modul1.acronym)
