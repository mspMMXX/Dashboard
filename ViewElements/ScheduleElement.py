import tkinter as tk


class ScheduleElement:

    def __init__(self, parent, schedule, remove_callback):
        self.schedule = schedule
        self.remove_callback = remove_callback
        self.frame = tk.Frame(parent, width=450, height=30, padx=10, pady=10)
        self.frame.pack_propagate(False)
        self.frame.pack()

        schedule_title_label = tk.Label(self.frame, text=f"Prüfungstermin: {schedule.schedule_title}")
        schedule_date_label = tk.Label(self.frame, text=str(schedule.schedule_date.strftime("%d.%m.%Y %H:%M")))
        remove_button = tk.Button(self.frame, text="Löschen", command=self.remove_schedule)

        schedule_title_label.grid(row=0, column=0, sticky="w")
        schedule_date_label.grid(row=0, column=1, sticky="w")
        remove_button.grid(row=0, column=2, sticky="e")

    def remove_schedule(self):
        self.remove_callback(self.schedule.schedule_id)
        self.frame.destroy()
