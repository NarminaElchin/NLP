import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('App studio')
root.geometry('200x200')

box = ttk.Combobox(root, values=["Russian", "Azerbaijani", "English", "French", "German", "Turkish", "Persian"])
box.pack()

root.mainloop()
