import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('nur.studio')
root.config(bg='red')
root.geometry('200x150')

def display():
    var.set(f'{box.current()}:{box.get()}')   # Display index value and content

var = tk.StringVar()                       # Define variables
var.set('')

label = tk.Label(root, textvariable=var)       # Create a label with the content as a variable
label.pack()

box = ttk.Combobox(root,  width=20,  values=["Russian", "Azerbaijani", "English", "French", "German", "Turkish", "Persian"])
box.pack()

btn = tk.Button(root, text='display', command=display)   #Create a button and execute the show function when the button is clicked

btn.pack()

root.mainloop()
