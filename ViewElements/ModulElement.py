import tkinter as tk


class ModulElement:

    def __init__(self, parent, acronym, image, title, status, exam_form, start_date, end_date, deadline, exam_date, grade):
        self.frame = tk.Frame(parent, width=450, height=200, bg="#5F6E78", padx=10, pady=10)
        self.frame.pack_propagate(False)
        self.frame.pack(pady=10)

        self.left_frame = tk.Frame(self.frame, bg="#5F6E78", width=150, height=200)
        self.left_frame.pack_propagate(False)
        self.left_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))

        self.right_frame = tk.Frame(self.frame, bg="#5F6E78")
        self.right_frame.pack_propagate(False)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=(5, 0))

        acronym_label = tk.Label(self.left_frame, text=acronym)
        modul_image = tk.Label(self.left_frame, width=150, height=150, bg="#5F2E73")

        acronym_label.pack(pady=10)
        modul_image.pack(pady=10)

        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(1, weight=1)

        title_label = tk.Label(self.right_frame, text="Titel")

        status_label = tk.Label(self.right_frame, text="Status")
        status_entry = tk.Entry(self.right_frame)

        exam_form_label = tk.Label(self.right_frame, text="Startdatum:")
        exam_form_entry = tk.Entry(self.right_frame)

        end_date_label = tk.Label(self.right_frame, text="Enddatum:")
        end_date_entry = tk.Entry(self.right_frame)

        deadline_label = tk.Label(self.right_frame, text="Deadline:")
        deadline_lbl = tk.Label(self.right_frame, text="Modulvariable")

        exam_date_label = tk.Label(self.right_frame, text="Prüfungstermin:")
        exam_date_entry = tk.Entry(self.right_frame)

        grade_label = tk.Label(self.right_frame, text="Note:")
        grade_entry = tk.Entry(self.right_frame)

        title_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="w")

        status_label.grid(row=1, column=0, sticky="w")
        status_entry.grid(row=1, column=1, sticky="w")
        status_entry.insert(0, status)

        exam_form_label.grid(row=2, column=0, sticky="w")
        exam_form_entry.grid(row=2, sticky="w")

        end_date_label.grid(row=3, column=0, sticky="w")
        end_date_entry.grid(row=3, column=1, sticky="w")

        deadline_label.grid(row=4, column=0, sticky="w")
        deadline_lbl.grid(row=4, column=1, sticky="w")

        exam_date_label.grid(row=5, column=0, sticky="w")
        exam_date_entry.grid(row=5, column=1, sticky="w")

        grade_label.grid(row=6, column=0, sticky="w")
        grade_entry.grid(row=6, column=1, sticky="w")

        self.frame.mainloop()


def main():
    root = tk.Tk()
    root.title("ModulElement Test")
    root.geometry("800x600")

    # Beispielbild (ersetzt "path_to_your_image.png" mit dem tatsächlichen Pfad)
    try:
        image = tk.PhotoImage(file="path_to_your_image.png")
    except Exception as e:
        print(f"Fehler beim Laden des Bildes: {e}")
        image = None

    # ModulElement hinzufügen
    modul_element = ModulElement(root, acronym="CS101", image=image, title="Computer Science 101", status="Active",
                                 exam_form="Written", start_date="2023-01-01", end_date="2023-06-01",
                                 deadline="2023-05-01", exam_date="2023-06-15", grade="A")

    root.mainloop()


if __name__ == "__main__":
    main()