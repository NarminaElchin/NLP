#Example: Create a dynamic platform to access information about various universities.

import webbrowser
from tkinter import *

def open_university(uni_name):
    university_urls = {
        "Oxford": "https://www.ox.ac.uk/",
        "Harvard": "https://www.harvard.edu/",
        "Cambridge": "https://www.cam.ac.uk/",
        "Stanford": "https://www.stanford.edu/"
    }
    webbrowser.open(university_urls.get(uni_name, "https://www.google.com"))  # Default to Google if not found

root = Tk()
root.title("University Application")
root.geometry("650x300")
root.config(bg='#b0ffff')

Button1 = Button(root, text="Oxford", bg="blue", fg="white", width=15, height=2, relief=RIDGE, bd=8, command=lambda: open_university("Oxford"))
Button1.place(x=10, y=20)

Button2 = Button(root, text="Harvard", bg="darkgrey", fg="black", width=15, height=2, relief=RIDGE, bd=8, command=lambda: open_university("Harvard"))
Button2.place(x=10, y=70)

Button3 = Button(root, text="Cambridge", bg="yellow", fg="black", width=15, height=2, relief=RIDGE, bd=8, command=lambda: open_university("Cambridge"))
Button3.place(x=10, y=120)

Button4 = Button(root, text="Stanford", bg="orange", fg="black", width=15, height=2, relief=RIDGE, bd=8, command=lambda: open_university("Stanford"))
Button4.place(x=10, y=170)

label_box1 = Label(root, text="Information about universities", font=("Arial", 12, "bold"),
                   bg="green", fg="black", width=40, height=10, relief=RIDGE, bd=14, anchor="center", wraplength=300)
label_box1.place(x=150, y=20)

root.mainloop()