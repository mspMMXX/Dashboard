import tkinter as tk
from ViewElements.ModulElement import ModulElement
from ViewElements.ScheduleElement import ScheduleElement
from Controller.DashboardController import DashboardController


class DashboardView:

    def __init__(self):
        self.controller = DashboardController()
        self.root = tk.Tk()
        self.root.title = "IU Dashboard"
        self.root.geometry("1490x950")

        left_frame = tk.Frame(self.root, width=496.6)
        center_frame = tk.Frame(self.root, width=496.6)
        right_frame = tk.Frame(self.root, width=496.6)

        left_frame.pack(side="left", fill="y")
        center_frame.pack(side="left", expand=True, fill="both")
        right_frame.pack(side="right", fill="y")

        # left_frame: Scrollbar mit Modulen
        canvas = tk.Canvas(left_frame, width=496.6)
        scrollbar = tk.Scrollbar(left_frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, width=496.6)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="n")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.modules = self.controller.get_modules()
        self.module_index = 0
        self.create_module_elements()

        # center_frame: Termine
        canvas_c = tk.Canvas(center_frame, width=496.6)
        scrollbar_c = tk.Scrollbar(center_frame, orient="vertical", command=canvas_c.yview)
        self.scrollable_frame_c = tk.Frame(canvas_c, width=496.6)

        self.scrollable_frame_c.bind(
            "<Configure>",
            lambda e: canvas_c.configure(
                scrollregion=canvas_c.bbox("all")
            )
        )

        canvas_c.create_window((0, 0), window=self.scrollable_frame_c, anchor="n")
        canvas_c.configure(yscrollcommand=scrollbar_c.set)

        canvas_c.pack(side="left", fill="both", expand=True)
        scrollbar_c.pack(side="right", fill="y")

        self.schedule_index = 0
        self.create_schedule_elements()

    def create_module_elements(self):
        for modul in self.modules:
            ModulElement(self.scrollable_frame, modul, self.create_schedule_elements)

    def create_schedule_elements(self):
        for widget in self.scrollable_frame_c.winfo_children():
            widget.destroy()
        schedules = self.controller.get_schedules()
        print("Schedule wurde aufgenommen")
        for schedule in schedules:
            print(f"Termin {schedule.schedule_date} wurde geladen")
            ScheduleElement(self.scrollable_frame_c, schedule)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = DashboardView()
    app.run()
