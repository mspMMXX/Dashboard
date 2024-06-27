import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class ModulElement:

    def __init__(self, parent, modul):
        self.frame = tk.Frame(parent, bg="#5F6E78", padx=10, pady=10)
        self.frame.pack(pady=10, fill="x")

        image = Image.open(modul.image_path)
