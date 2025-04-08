from tkinter import *
from PIL import Image, ImageTk
import webbrowser
import pyttsx3
from datetime import datetime

def websites(website_name):
    website_urls = {
        "WhatsApp": "https://web.whatsapp.com/",
        "LinkedIn": "https://www.linkedin.com/login",
        "YouTube": "https://www.youtube.com/",
        "FaceBook": "https://www.facebook.com/login.php/"
    }
    webbrowser.open(website_urls.get(website_name, "https://www.google.com"))  # Default to Google if not found

root = Tk()
root.title('my application')
root.geometry("700x400")

# Load the background robot image
bg_image = Image.open('robot.jpg')
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Cover entire window

# Create a frame for the buttons on the left
left_frame = Frame(root, bg='white')
left_frame.pack(side=LEFT, fill=Y, padx=10, pady=10)

# Load and resize social media logos (adjust size as needed)
logo_size = (70, 70)  # Width, Height in pixels

# WhatsApp
whatsapp_frame = Frame(left_frame, bg='white')
whatsapp_frame.pack(pady=(5))  # 0 padding at top, 30 below
whatsapp_img = Image.open('WhatsApp.jpg').resize(logo_size, Image.Resampling.LANCZOS)
whatsapp_photo = ImageTk.PhotoImage(whatsapp_img)
whatsapp_btn = Button(left_frame, image=whatsapp_photo, command=lambda: websites("WhatsApp"), borderwidth=0)
whatsapp_btn.pack(pady=5)
whatsapp_btn.image = whatsapp_photo  # Keep reference

# LinkedIn
linkedin_frame = Frame(left_frame, bg='white')
linkedin_frame.pack(pady=5)  # 8 pixels above and below
linkedin_img = Image.open('LinkedIn.jpg').resize(logo_size, Image.Resampling.LANCZOS)
linkedin_photo = ImageTk.PhotoImage(linkedin_img)
linkedin_btn = Button(left_frame, image=linkedin_photo, command=lambda: websites("LinkedIn"), borderwidth=0)
linkedin_btn.pack(pady=5)
linkedin_btn.image = linkedin_photo

# YouTube
youtube_frame = Frame(left_frame, bg='white')
youtube_frame.pack(pady=5)
youtube_img = Image.open('YouTube.jpg').resize(logo_size, Image.Resampling.LANCZOS)
youtube_photo = ImageTk.PhotoImage(youtube_img)
youtube_btn = Button(left_frame, image=youtube_photo, command=lambda: websites("YouTube"), borderwidth=0)
youtube_btn.pack(pady=5)
youtube_btn.image = youtube_photo

# Facebook
facebook_frame = Frame(left_frame, bg='white')
facebook_frame.pack(pady=5)
facebook_img = Image.open('FaceBook.jpg').resize(logo_size, Image.Resampling.LANCZOS)
facebook_photo = ImageTk.PhotoImage(facebook_img)
facebook_btn = Button(left_frame, image=facebook_photo, command=lambda: websites("FaceBook"), borderwidth=0)
facebook_btn.pack(pady=5)
facebook_btn.image = facebook_photo

# Keep reference to background image
bg_label.image = bg_photo

root.mainloop()