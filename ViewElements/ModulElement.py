import tkinter as tk


class ModulElement:

    def __init__(self, parent, modul):
        self.frame = tk.Frame(parent, height="200", width="450", bg="#5F6E78", padx=10, pady=10)
        self.frame.pack(pady=10, fill="x")

        self.label = tk.Label(self.frame, text=modul.title)
