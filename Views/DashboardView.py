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

        canvas = tk.Canvas(left_frame, background="#87CEEB", width=496.6)
        scrollbar = tk.Scrollbar(left_frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, background="#87CEEB", width=496.6)

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

    def create_module_elements(self):
        if self.module_index < len(self.modules):
            modul = self.modules[self.module_index]
            print(f"Zeige ModulElement: {modul.acronym}, {modul.title}")
            ModulElement(self.scrollable_frame, modul)
            self.module_index += 1
            self.root.after(100, self.create_module_elements)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = DashboardView()
    app.run()