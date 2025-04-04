import tkinter as tk
import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech (higher is faster)
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Function to handle the button click event
def speak_text():
    text = entry.get()  # Get text from the entry widget
    if text:
        engine.say(text)  # Speak the entered text
        engine.runAndWait()  # Wait until the speech is finished

# Create the main window
root = tk.Tk()
root.title("Text to Speech")
root.geometry("400x250")

# Create a label
label = tk.Label(root, text="Enter text to speak:")
label.pack(pady=10)

# Create a text entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a button to trigger the speech
button = tk.Button(root, text="Speak", command=speak_text)
button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()