class Schedule:
    """
    Eine Klasse, die einen Zeitplan (Schedule) repräsentiert.
    """

    def __init__(self, db, title, schedule_date, student_id):
        """
        Initialisiert ein Schedule-Objekt.
        Args:
            db: Die Datenbankverbindung.
            title: Der Titel des Zeitplans.
            schedule_date: Das Datum des Zeitplans.
            student_id: Die ID des Studenten, zu dem der Zeitplan gehört.
        """
        self.db = db
        self.title = title
        self.schedule_date = schedule_date
        self.student_id = student_id
        self.id = None

    def save(self):
        """
        Speichert den Zeitplan in der Datenbank.
        Wenn der Zeitplan bereits existiert, wird er aktualisiert. Andernfalls wird ein neuer Zeitplan erstellt.
        """
        if self.id is None:
            query = """
            INSERT INTO Schedule (title, schedule_date, student_id)
            VALUES (%s, %s, %s)
            """
            params = (self.title, self.schedule_date, self.student_id)
            self.db.execute_query(query, params)
            self.id = self.db.cursor.lastrowid
        else:
            query = """
            UPDATE Schedule
            SET title = %s, schedule_date = %s
            WHERE id = %s
            """
            params = (self.title, self.schedule_date, self.id)
            self.db.execute_query(query, params)

    def load(self, schedule_id):
        """
        Lädt die Daten eines Zeitplans aus der Datenbank basierend auf der Zeitplan-ID.
        Args:
            schedule_id: Die ID des zu ladenden Zeitplans.
        """
        query = "SELECT * FROM Schedule WHERE id = %s"
        params = (schedule_id,)
        result = self.db.fetch_one(query, params)
        if result:
            self.id = result['id']
            self.title = result['title']
            self.schedule_date = result['schedule_date']
            self.student_id = result['student_id']

    @classmethod
    def from_dict(cls, data):
        """
        Erstellt ein Schedule-Objekt aus einem Dictionary.
        Args:
            data: Ein Dictionary mit den Daten des Zeitplans.
        Returns:
            Ein Schedule-Objekt, das die Daten aus dem Dictionary enthält.
        """
        schedule = cls(None, data['title'], data['schedule_date'], data['student_id'])
        schedule.id = data['id']
        return schedule
