import tkinter as tk
import pyttsx3
from tkinter import filedialog

# Create a Tkinter window
root = tk.Tk()
root.title("Speech Output Application")

# Start the pyttsx3 speech engine
engine = pyttsx3.init()

# Voice engine parameters
engine.setProperty('rate', 150) # Speed (default 200)
engine.setProperty('volume', 1) # Pitch (between 0.0 and 1.0)

# We set the voice engines for speaking in different languages
voices = engine.getProperty('voices')

# ComboBox for different voice options (for the user to choose a voice)
def change_voice(voice_id):
    engine.setProperty('voice', voices[voice_id].id)

# Speech function
def speak_text():
    text = text_entry.get() # Get the input text gets
    engine.say(text) # Reads text
    engine.runAndWait() # Starts the speaker

# Read text from file function
def read_from_file():
    file_path = filedialog.askopenfilename(title="Choose file", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
            text_entry.delete(0, tk.END) # Clear the existing text field
            text_entry.insert(tk.END, text) # Insert the text read from the file
            # Create a text entry in the Tkinter window
text_entry = tk.Entry(root, width=40)
text_entry.pack(pady=10)

# Create a button in the Tkinter window
speak_button = tk.Button(root, text="Speak", command=speak_text)
speak_button.pack(pady=10)

# Button to read text from file
file_button = tk.Button(root, text="Read from file", command=read_from_file)
file_button.pack(pady=10)

# ComboBox for language selection
voice_label = tk.Label(root, text="Select Voice:")
voice_label.pack(pady=5)

voice_combo = tk.OptionMenu(root, *[voice.name for voice in voices], command=lambda voice: change_voice(voices.index(voice)))
voice_combo.pack(pady=5)

# A slider to adjust the voice speed
def change_rate(val):
    engine.setProperty('rate', int(val))
rate_slider = tk.Scale(root, from_=50, to_=300, orient="horizontal", label="Voice Speed", command=change_rate)
rate_slider.set(150) # Initial speed
rate_slider.pack(pady=10)

# Height adjustment
def change_volume(val):
    engine.setProperty('volume', float(val))
volume_slider = tk.Scale(root, from_=0.0, to_=1.0, orient="horizontal", resolution=0.1, label="Volume", command=change_volume)
volume_slider.set(1.0) # Initial height
volume_slider.pack(pady=10)

# Launch Tkinter window
root.mainloop()