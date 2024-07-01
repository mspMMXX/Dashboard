import tkinter as tk
from ViewElements.ModulElement import ModulElement
from Controller.DashboardController import DashboardController


class DashboardView:

    def __init__(self):
        self.controller = DashboardController()
        self.root = tk.Tk()
        self.root.title = "IU Dashboard"
        self.root.geometry("1490x950")

        left_frame = tk.Frame(self.root, background="#B0C4DE", width=496.6)
        center_frame = tk.Frame(self.root, background="#87CEEB", width=496.6)
        right_frame = tk.Frame(self.root, background="#B0C4DE", width=496.6)

        left_frame.pack(side="left", fill="y")
        center_frame.pack(side="left", expand=True, fill="both")
        right_frame.pack(side="right", fill="y")

        modules = self.controller.get_modules()
        for modul in modules:
            ModulElement(left_frame, modul)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = DashboardView()
    app.run()