import tkinter as tk


class ScheduleElement:

    def __init__(self, parent, schedule):
        self.schedule = schedule
        self.frame = tk.Frame(parent, width=450, height=30, padx=10, pady=10)
        self.frame.pack_propagate(False)
        self.frame.pack()

        schedule_title_label = tk.Label(self.frame, text=schedule.schedule_title)
        schedule_date_label = tk.Label(self.frame, text=str(schedule.schedule_date.strftime("%d.%m.%Y")))

        schedule_title_label.grid(row=0, column=0, sticky="w")
        schedule_date_label.grid(row=0, column=1, sticky="w")
