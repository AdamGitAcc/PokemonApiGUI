import tkinter as tk
from tkinter import ttk

root = tk.Tk()

window_width = 1000
window_height = 700

window_max_width = root.winfo_screenwidth()
window_max_height = root.winfo_screenheight()


center_width = int(root.winfo_screenwidth() / 2 - window_width / 2)
center_height = int(root.winfo_screenheight() / 2 - window_height / 2)


