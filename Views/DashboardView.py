import tkinter as tk
from tkinter import font as tkfont
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

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.modules = self.controller.get_modules()
        self.module_index = 0
        self.create_module_elements()

        # center_frame: Termine
        schedule_title_label = tk.Label(center_frame, text="Terminname:")
        self.schedule_entry = tk.Entry(center_frame)

        schedule_date_label = tk.Label(center_frame, text="Datum")
        self.schedule_date_entry = tk.Entry(center_frame)

        add_schedule_button = tk.Button(center_frame, text="Neu", command=self.create_new_schedule)

        schedule_title_label.grid(row=0, column=0)
        self.schedule_entry.grid(row=0, column=1)
        schedule_date_label.grid(row=0, column=2)
        self.schedule_date_entry.grid(row=0, column=3)
        add_schedule_button.grid(row=0, column=4)

        canvas_c = tk.Canvas(center_frame, width=496.6)
        scrollbar_c = tk.Scrollbar(center_frame, orient="vertical", command=canvas_c.yview)
        self.scrollable_frame_c = tk.Frame(canvas_c, width=496.6)

        self.scrollable_frame_c.bind(
            "<Configure>",
            lambda e: canvas_c.configure(
                scrollregion=canvas_c.bbox("all")
            )
        )

        canvas_c.create_window((0, 0), window=self.scrollable_frame_c, anchor="nw")
        canvas_c.configure(yscrollcommand=scrollbar_c.set)

        canvas_c.grid(row=1, column=0, columnspan=5, sticky="nsew")
        scrollbar_c.grid(row=1, column=5, sticky="ns")

        center_frame.grid_rowconfigure(1, weight=1)
        center_frame.grid_columnconfigure(1, weight=1)

        self.schedule_index = 0
        self.create_schedule_elements()

        # right_frame: Übersicht
        # Notendurchschnitt
        title_font = tkfont.Font(size=14, weight="bold")

        avg_grade_title = tk.Label(right_frame, text="Notendurchschnitt", pady=15, font=title_font)
        avg_grade_title.grid(row=0, column=1, sticky="e")

        planned_grade_label = tk.Label(right_frame, text="Geplant:")
        planned_grade_entry = tk.Entry(right_frame)
        actual_grade_label = tk.Label(right_frame, text="Momentan:")
        actual_grade_lbl = tk.Label(right_frame, text=self.get_actual_avg_grade())

        planned_grade_label.grid(row=1, column=0, sticky="w")
        planned_grade_entry.grid(row=1, column=1, sticky="e")
        actual_grade_label.grid(row=2, column=0, sticky="w")
        actual_grade_lbl.grid(row=2, column=1, sticky="e")

        # Studium
        study_label = tk.Label(right_frame, text="Studium", pady=15, font=title_font)
        study_name_label = tk.Label(right_frame, text="Studiengang:")
        study_name_lbl = tk.Label(right_frame, text="Softwareentwicklung")
        study_duration_label = tk.Label(right_frame, text="Studiendauer:")
        study_duration_lbl = tk.Label(right_frame, text="Variable")
        study_start_label = tk.Label(right_frame, text="Studienbeginn:")
        study_start_lbl = tk.Label(right_frame, text="Variable")
        study_end_label = tk.Label(right_frame, text="Abschluss:")
        study_end_lbl = tk.Label(right_frame, text="Variable")
        expected_end_label = tk.Label(right_frame, text="Voraussichtlicher Abschluss:")
        expected_end_lbl = tk.Label(right_frame, text="Variable")

        study_label.grid(row=3, column=1, sticky="e")
        study_name_label.grid(row=4, column=0, sticky="w")
        study_name_lbl.grid(row=4, column=1, sticky="e")
        study_duration_label.grid(row=5, column=0, sticky="w")
        study_duration_lbl.grid(row=5, column=1, sticky="e")
        study_start_label.grid(row=6, column=0, sticky="w")
        study_start_lbl.grid(row=6, column=1, sticky="e")
        study_end_label.grid(row=7, column=0, sticky="w")
        study_end_lbl.grid(row=7, column=1, sticky="e")
        expected_end_label.grid(row=8, column=0, sticky="w")
        expected_end_lbl.grid(row=8, column=1, sticky="e")

        # IU-Kontaktdaten
        contact_title = tk.Label(right_frame, text="IU-Kontaktdaten", font=title_font)
        study_advisory_label = tk.Label(right_frame, text="Studienberatung:")
        study_advisory_lbl = tk.Label(right_frame, text="Variable")
        exam_service_label = tk.Label(right_frame, text="Prüfungsservice")
        exam_service_lbl = tk.Label(right_frame, text="Variable")
        study_coach_label = tk.Label(right_frame, text="Study Coach:")
        study_coach_lbl = tk.Label(right_frame, text="Variable")
        career_service_label = tk.Label(right_frame, text="Career Service:")
        career_service_lbl = tk.Label(right_frame, text="Variable")

        contact_title.grid(row=9, column=1, sticky="e", pady=15)
        study_advisory_label.grid(row=10, column=0, sticky="w")
        study_coach_lbl.grid(row=10, column=1, sticky="e")
        exam_service_label.grid(row=11, column=0, sticky="w")
        exam_service_lbl.grid(row=11, column=1, sticky="e")
        study_coach_label.grid(row=12, column=0, sticky="w")
        study_coach_lbl.grid(row=12, column=1, sticky="e")
        career_service_label.grid(row=13, column=0, sticky="w")
        career_service_lbl.grid(row=13, column=1, sticky="e")

        # Student
        student_title = tk.Label(right_frame, text="Student", font=title_font)
        last_name_label = tk.Label(right_frame, text="Nachname:")
        last_name_lbl = tk.Label(right_frame, text="Variable")
        first_name_label = tk.Label(right_frame, text="Vorname:")
        first_name_lbl = tk.Label(right_frame, text="Variable")
        student_number_label = tk.Label(right_frame, text="Martrikelnummer:")
        student_number_lbl = tk.Label(right_frame, text="Variable")

        student_title.grid(row=14, column=1, sticky="e", pady=15)
        last_name_label.grid(row=15, column=0, sticky="w")
        last_name_lbl.grid(row=15, column=1, sticky="e")
        first_name_label.grid(row=16, column=0, sticky="w")
        first_name_lbl.grid(row=16, column=1, sticky="e")
        student_number_label.grid(row=17, column=0, sticky="w")
        student_number_lbl.grid(row=17, column=1, sticky="e")
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
            ScheduleElement(self.scrollable_frame_c, schedule, self.controller.delete_schedule)

    def create_new_schedule(self):
        self.controller.create_new_schedule(self.schedule_entry.get(), self.schedule_date_entry.get())
        self.create_schedule_elements()
        self.schedule_entry.delete(0, tk.END)
        self.schedule_date_entry.delete(0, tk.END)

    def get_actual_avg_grade(self):
        return str(5)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = DashboardView()
    app.run()
