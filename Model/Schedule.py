class Schedule:
    def __init__(self, db, title, schedule_date, student_id):
        self.db = db
        self.title = title
        self.schedule_date = schedule_date
        self.student_id = student_id
        self.id = None

    def save(self):
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
        query = "SELECT * FROM Schedule WHERE id = %s"
        params = (schedule_id,)
        result = self.db.fetch_one(query, params)
        if result:
            self.id = result['id']
            self.title = result['title']
            self.schedule_date = result['schedule_date']
            self.student_id = result['student_id']

    def delete(self):
        if self.id:
            query = "DELETE FROM Schedule WHERE id = %s"
            params = (self.id,)
            self.db.execute_query(query, params)
            self.id = None

    @classmethod
    def from_dict(cls, data):
        schedule = cls(None, data['title'], data['schedule_date'], data['student_id'])
        schedule.id = data['id']
        return schedule
