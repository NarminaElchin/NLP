from tkinter import *
from PIL import Image, ImageTk
import webbrowser
import pyttsx3
from datetime import datetime

def update_time():
    # Get current time and format it
    current_time = datetime.now().strftime("%H:%M:%S")
    # Update the text on the canvas
    canvas.itemconfig(time_text, text=current_time)
    # Schedule the function to run again after 1000ms (1 second)
    root.after(1000, update_time)

def websites(website_name):
    website_urls = {
        "WhatsApp": "https://web.whatsapp.com/",
        "LinkedIn": "https://www.linkedin.com/login",
        "YouTube": "https://www.youtube.com/",
        "FaceBook": "https://www.facebook.com/login.php/"
    }
    webbrowser.open(website_urls.get(website_name, "https://www.google.com"))  # Default to Google if not found


root = Tk()
root.title('My Application')
root.geometry("1300x700")

# Load the robot image with the social media icons
image = Image.open('my_robut.jpeg')
photo = ImageTk.PhotoImage(image)

# Create a canvas to place the image and text
canvas = Canvas(root, width=1300, height=700, highlightthickness=0)
canvas.pack()

# Place the robot image on the canvas
canvas.create_image(650, 350, image=photo)  # Centered in the 1300x700 window

# Get current time and format it
current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# Add current time at the top center of the image
time_text = canvas.create_text(650, 50, text="", font=('Arial', 20, 'bold'), fill='black')  # Top center
update_time()  # Start the time update loop

# Create a white square background for the text
text_x, text_y = 727, 377  # Coordinates for the text
square_size = 120  # Adjust this to change the size of the square
canvas.create_rectangle(
    text_x - square_size // 2,  # Left edge
    text_y - square_size // 2,  # Top edge
    text_x + square_size // 2,  # Right edge
    text_y + square_size // 2,  # Bottom edge
    fill="white", outline="white"  # White fill with optional black border
)

# Place the "I am Narmina's slave" text on top of the square
canvas.create_text(text_x, text_y, text="I am Narmina's slave", font=('Arial', 11, 'bold'), fill='black')

# Add current time at the top of the image
label_data = Label(root, text=current_time,
                font = ('Arial', 20, 'bold'), fg='red',
                   bg = 'black', image = photo, compound = 'bottom', anchor='w')

# Add transparent buttons over the existing social media icons
button_width = 60  # Approximate width of the icons
button_height = 60  # Approximate height of the icons

# WhatsApp button (topmost icon)
whatsapp_btn = Button(canvas, command=lambda: websites("WhatsApp"), bg='white', bd=0, highlightthickness=0)
canvas.create_window(210, 120, window=whatsapp_btn, width=button_width, height=button_height)

# LinkedIn button (second icon)
linkedin_btn = Button(canvas, command=lambda: websites("LinkedIn"), bg='white', bd=0, highlightthickness=0)
canvas.create_window(210, 260, window=linkedin_btn, width=button_width, height=button_height)

# YouTube button (third icon)
youtube_btn = Button(canvas, command=lambda: websites("YouTube"), bg='white', bd=0, highlightthickness=0)
canvas.create_window(210, 400, window=youtube_btn, width=button_width, height=button_height)

# Facebook button (bottom icon)
facebook_btn = Button(canvas, command=lambda: websites("FaceBook"), bg='white', bd=0, highlightthickness=0)
canvas.create_window(210, 540, window=facebook_btn, width=button_width, height=button_height)

# Make the buttons transparent
for btn in [whatsapp_btn, linkedin_btn, youtube_btn, facebook_btn]:
    btn.configure(bg=root.cget("bg"), activebackground=root.cget("bg"))

# Start the pyttsx3 speech engine (moved here to run before mainloop)
engine = pyttsx3.init()

# Voice engine parameters
engine.setProperty('rate', 150) # Speed (default 200)
engine.setProperty('volume', 1) # Pitch (between 0.0 and 1.0)

# We set the voice engines for speaking in different languages
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

root.update()  # Ensure the window is rendered before speaking
engine.say("I am Narmina's slave")
engine.runAndWait() # Speak the text after the image is displayed

root.mainloop()