from tkinter \
import *

root = Tk()
root.title('nur application')
root.geometry("700x400")
photo = PhotoImage(file='meow-im-dancing.gif')
label_data = Label(root, text="meow meow",
                font = ('Arial', 20, 'bold'), fg='yellow',
                   bg = 'black', image = photo, compound = 'bottom', anchor='w')
label_data.pack()
#label_data.place(x=70, y=10)

root.mainloop()