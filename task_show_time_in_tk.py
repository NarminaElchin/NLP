from tkinter import *
import time

def gettime():
      date = time.strftime("%d-%m-%Y %H:%M:%S") # Get the current time and convert it to a string
      label.configure(text=date)   # Reset label text
      window.after(1000,gettime) # Call the function gettime every 1s to get the time by itself

window = Tk()
window.geometry("1100x200")
window.title('clock')

label = Label(window,text='',fg='red',font=("black body",80), bg="black"  )
label.place(x=40, y=20)
gettime()
window.mainloop()
