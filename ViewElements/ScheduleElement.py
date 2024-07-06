import tkinter as tk
from Model.Schedule import Schedule


class ScheduleElement:
    def __init__(self, parent, schedule_data, remove_callback):
        """
        Initialisiert ein ScheduleElement.

        Args:
            parent (tk. Widget): Das übergeordnete Tkinter-Widget.
            schedule_data (dict): Die Daten des Termins.
            remove_callback (function): Die Callback-Funktion zum Entfernen des Termins.
        """
        self.schedule = Schedule.from_dict(schedule_data)  # Erstellt ein Schedule-Objekt aus den Daten
        self.remove_callback = remove_callback  # Speichert die Callback-Funktion

        # Frame für das Termin-Element erstellen
        self.frame = tk.Frame(parent, width=450, height=30, padx=10, pady=10)
        self.frame.pack_propagate(False)
        self.frame.pack()

        # Label für den Titel des Termins
        schedule_title_label = tk.Label(self.frame, text=f"Prüfungstermin: {self.schedule.title}")

        # Label für das Datum des Termins
        schedule_date_label = tk.Label(self.frame, text=str(self.schedule.schedule_date.strftime("%d.%m.%Y %H:%M")))

        # Button zum Löschen des Termins
        remove_button = tk.Button(self.frame, text="Löschen", command=self.remove_schedule)

        # Platzierung der Widgets im Grid-Layout
        schedule_title_label.grid(row=0, column=0, sticky="w")
        schedule_date_label.grid(row=0, column=1, sticky="w")
        remove_button.grid(row=0, column=2, sticky="e")

    def remove_schedule(self):
        """
        Entfernt den Termin und zerstört das Frame-Widget.
        """
        self.remove_callback(self.schedule.id)  # Ruft die Callback-Funktion auf, um den Termin zu entfernen
        self.frame.destroy()  # Zerstört das Frame-Widget
