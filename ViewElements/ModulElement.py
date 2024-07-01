import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from Model.Student import Student
from datetime import datetime
import os


class ModulElement:

    def __init__(self, parent, modul):
        self.modul = modul  # Speichern Sie `modul` als Instanzvariable
        self.frame = tk.Frame(parent, width=450, height=220, bg="#5F6E78", padx=10, pady=10)
        self.frame.pack_propagate(False)
        self.frame.pack(pady=10)

        self.left_frame = tk.Frame(self.frame, bg="#5F6E78", width=150, height=200)
        self.left_frame.pack_propagate(False)
        self.left_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))

        image_path = modul.image_path
        if not os.path.exists(image_path):
            print(f"Bilddatei nicht gefunden: {image_path}")
            image = None
        else:
            try:
                image = PhotoImage(file=image_path)
            except Exception as e:
                print(f"Fehler beim Darstellen des Bildes: {e}")
                image = None

        acronym_label = tk.Label(self.left_frame, text=modul.acronym, bg="#5F6E78", fg="white")
        modul_image = tk.Label(self.left_frame, image=image, width=150, height=150, bg="#5F6E78")
        modul_image.image = image

        acronym_label.pack()
        modul_image.pack()

        self.right_frame = tk.Frame(self.frame, bg="#5F6E78")
        self.right_frame.pack_propagate(False)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=(5, 0))

        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1, minsize=120)
        self.right_frame.grid_columnconfigure(1, weight=1)

        title_label = tk.Label(self.right_frame, text=modul.title, bg="#5F6E78", fg="white")

        # Erstelle das Status-Oval und speichere die ID des Ovals
        self.status_oval = tk.Canvas(self.right_frame, width=25, height=25, bg="#5F6E78", highlightthickness=0)
        if modul.status == "Offen":
            fill_status = "gray"
        elif modul.status == "In Bearbeitung":
            fill_status = "orange"
        else:
            fill_status = "green"
        self.oval_id = self.status_oval.create_oval(5, 5, 20, 20, fill=fill_status)

        self.status_var = tk.StringVar()
        self.status_var.set(modul.status)
        status_dropdown = ttk.Combobox(self.right_frame, textvariable=self.status_var)
        status_dropdown['values'] = ("Offen", "In Bearbeitung", "Abgeschlossen")
        status_dropdown.current(0)

        # Binde die Methode an das Ändern des Dropdown-Menüwerts
        status_dropdown.bind("<<ComboboxSelected>>", self.update_modul)

        exam_form_label = tk.Label(self.right_frame, text="Prüfungsform:", bg="#5F6E78", fg="white")
        exam_form_lbl = tk.Label(self.right_frame, text=modul.exam_format, bg="#5F6E78", fg="white")

        start_date_label = tk.Label(self.right_frame, text="Startdatum:", bg="#5F6E78", fg="white")
        self.start_date_lbl = tk.Label(self.right_frame, bg="#5F6E78", fg="white")
        if modul.start_date:
            self.start_date_lbl.config(text=modul.start_date.strftime('%Y-%m-%d'))

        end_date_label = tk.Label(self.right_frame, text="Enddatum:", bg="#5F6E78", fg="white")
        self.end_date_lbl = tk.Label(self.right_frame, bg="#5F6E78", fg="white")
        if modul.end_date:
            self.end_date_lbl.config(text=modul.end_date.strftime('%Y-%m-%d'))

        deadline_label = tk.Label(self.right_frame, text="Deadline:", bg="#5F6E78", fg="white")
        self.deadline_lbl = tk.Label(self.right_frame, bg="#5F6E78", fg="white")
        if modul.deadline:
            self.deadline_lbl.config(text=modul.deadline.strftime('%Y-%m-%d'))

        exam_date_label = tk.Label(self.right_frame, text="Prüfungstermin:", bg="#5F6E78", fg="white")
        exam_date_entry = tk.Entry(self.right_frame)

        grade_label = tk.Label(self.right_frame, text="Note:", bg="#5F6E78", fg="white")
        grade_entry = tk.Entry(self.right_frame)

        title_label.grid(row=0, column=0, columnspan=2, sticky="w")

        self.status_oval.grid(row=1, column=0, sticky="w")
        status_dropdown.grid(row=1, column=1, sticky="w")

        exam_form_label.grid(row=2, column=0, sticky="w")
        exam_form_lbl.grid(row=2, column=1, sticky="w")

        start_date_label.grid(row=3, column=0, sticky="w")
        self.start_date_lbl.grid(row=3, column=1, sticky="w")

        end_date_label.grid(row=4, column=0, sticky="w")
        self.end_date_lbl.grid(row=4, column=1, sticky="w")

        deadline_label.grid(row=5, column=0, sticky="w")
        self.deadline_lbl.grid(row=5, column=1, sticky="w")

        exam_date_label.grid(row=6, column=0, sticky="w")
        exam_date_entry.grid(row=6, column=1, sticky="w")

        grade_label.grid(row=7, column=0, sticky="w")
        grade_entry.grid(row=7, column=1, sticky="w")

    # Methode zur Aktualisierung des Status-Ovals
    def update_modul(self, event):
        new_status = self.status_var.get()
        self.modul.set_status(new_status)
        self.modul.set_start_date()
        self.modul.set_end_date()

        student = Student(last_name="Mustermann", first_name="Max", study_duration=3, study_start_date=datetime(2024, 1, 3))
        self.modul.set_deadline(student)

        if new_status == "Abgeschlossen":
            self.modul.set_end_date()
        else:
            self.modul.end_date = None

        if new_status == "Offen":
            fill_status = "gray"
        elif new_status == "In Bearbeitung":
            fill_status = "orange"
        else:
            fill_status = "green"

        self.status_oval.itemconfig(self.oval_id, fill=fill_status)

        # Aktualisiert das Startdatum-Label
        if new_status == "In Bearbeitung":
            if self.modul.start_date:
                self.start_date_lbl.config(text=self.modul.start_date.strftime('%Y-%m-%d'))
            else:
                self.start_date_lbl.config(text="")

            # Aktualisiert das Deadline-Label
            if self.modul.deadline:
                self.deadline_lbl.config(text=self.modul.deadline.strftime('%Y-%m-%d'))
            else:
                self.deadline_lbl.config(text="")

        if self.modul.end_date:
            self.end_date_lbl.config(text=self.modul.end_date.strftime('%Y-%m-%d'))
        else:
            self.end_date_lbl.config(text="")
