import tkinter as tk
from ViewElements import ModulElement


class DashboardView:
    root = tk.Tk()
    root.title = "IU Dashboard"
    root.geometry("1490x950")

    left_frame = tk.Frame(root, background="#B0C4DE", width=496.6)
    center_frame = tk.Frame(root, background="#87CEEB", width=496.6)
    right_frame = tk.Frame(root, background="#B0C4DE", width=496.6)

    left_frame.pack(side="left", fill="y")
    center_frame.pack(side="left", expand=True, fill="both")
    right_frame.pack(side="right", fill="y")

    root.mainloop()
