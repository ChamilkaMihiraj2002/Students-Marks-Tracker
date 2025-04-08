import tkinter as tk

class Marks(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="📄 Marks", font=("Arial", 18))
        label.pack(pady=20)

        btn = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage"))
        btn.pack()