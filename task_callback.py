from tkinter import*

app = Tk()

app.geometry("200x150")
def callback():
    mylabel.config(text="duck off")


mylabel = Label(app, text="wassup nigga", bg="red")
mylabel.place(x=40, y=20)
mybutton = Button(app, text="Click Me", command=callback)
mybutton.place(x=40, y=50)

app.mainloop()