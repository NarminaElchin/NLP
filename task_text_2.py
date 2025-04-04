from tkinter import*

app = Tk()
app.title('n app')
# Use StringVar as the widget variable.
# value : Option to set initial value.
# Assigns 'test' to stringVar as the initial value.
# If value="test" is not set, '' will be assigned as the initial value.
#var = StringVar(value="test") # Create a text variable
# set: Change the value from 'test' to 'hello nur'.
# First argument: The string to set
#var.set('wassup nigga') # set content
label_data = Label(app, text="wassup nigga", font=('Arial',24)) # The content is variable a
label_data.pack()
#var.get()
app.mainloop()
