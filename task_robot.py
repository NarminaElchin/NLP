from tkinter import *
from PIL import Image, ImageTk
import webbrowser

def websites(website_name):
    website_urls = {
        "WhatsApp": "https://web.whatsapp.com/",
        "LinkedIn": "https://www.linkedin.com/login",
        "YouTube": "https://www.youtube.com/",
        "FaceBook": "https://www.facebook.com/login.php/"
    }
    webbrowser.open(website_urls.get(website_name, "https://www.google.com"))  # Default to Google if not found


def on_canvas_click(event):
    x, y = event.x, event.y
    # Define clickable regions based on where the icons are on the image
    if 50 <= x <= 100 and 100 <= y <= 150:  # WhatsApp region
        websites("WhatsApp")
    elif 50 <= x <= 100 and 200 <= y <= 250:  # LinkedIn region
        websites("LinkedIn")
    elif 50 <= x <= 100 and 300 <= y <= 350:  # YouTube region
        websites("YouTube")
    elif 50 <= x <= 100 and 400 <= y <= 450:  # Facebook region
        websites("FaceBook")


root = Tk()
root.title('my application')
root.geometry("1300x700")

image = Image.open('my_robut.jpeg')

photo = ImageTk.PhotoImage(image)

# Create a Canvas widget to hold the image and text
canvas = Canvas(root, width=image.width, height=image.height)
canvas.pack()

canvas.create_image(0, 0, anchor='nw', image=photo)

# Add text with border effect on the chest of the robot
text = "I am a robot"
font = ('Arial', 20, 'bold')
text_id = canvas.create_text(image.width//2, image.height//2, text=text, font=font, fill="yellow", anchor="center")

canvas.create_text(image.width//2, image.height//2, text=text, font=font, fill="black", anchor="center", offset="-2,-2")
canvas.create_text(image.width//2, image.height//2, text=text, font=font, fill="black", anchor="center", offset="2,-2")
canvas.create_text(image.width//2, image.height//2, text=text, font=font, fill="black", anchor="center", offset="-2,2")
canvas.create_text(image.width//2, image.height//2, text=text, font=font, fill="black", anchor="center", offset="2,2")

# Create a Frame on the left side for website buttons
frame = Frame(root)
frame.pack(side=LEFT, padx=20)

root.mainloop()


###add the website urls to picture
