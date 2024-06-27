import uuid


class Schedule:

    def __init__(self, schedule_title, schedule_date):
        self.schedule_id = uuid.uuid4()
        self.schedule_title = schedule_title
        self.schedule_date = schedule_date
