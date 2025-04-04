from tkinter import *
from PIL import Image, ImageTk
import webbrowser

def open_website(website_name):
    websites = {
        "WhatsApp": "https://web.whatsapp.com/",
        "LinkedIn": "https://www.linkedin.com/login",
        "YouTube": "https://www.youtube.com/",
        "Facebook": "https://www.facebook.com/login.php/"
    }
    webbrowser.open(websites.get(website_name, ""))

root = Tk()
root.title('my application')
root.geometry("1300x800")
image = Image.open('my_robut.jpeg')

photo = ImageTk.PhotoImage(image)


root.mainloop()