from tkinter import *
app = Tk()
#Function to execute when button is clicked
def change_text():
    var.set("Button Clicked") #Update variable
#Set StringVar
var = StringVar(value="variable")

#Label
lab_data = Label(app,relief="raised",textvariable=var)  #Set textvariable
lab_data.pack()

#Button
but_data = Button(app, text="click", command=change_text) #Function to execute when button is clicked
but_data.pack()

app.mainloop()