import tkinter as tk
from tkinter import Label, Frame, Button
from PIL import Image, ImageTk
import pyttsx3
import threading

def speak_language_info(language_info):
    engine = pyttsx3.init()
    engine.say(language_info)
    engine.runAndWait()

def blink_robot(count=6):
    if count > 0:
        color = "green" if count % 2 == 0 else "red"
        robot_label.config(bg=color)
        root.after(500, blink_robot, count - 1)
    else:
        robot_label.config(bg="white")

def on_flag_click(country, language_info):
    info_label.config(text=f"{country} dili: {language_info}")
    threading.Thread(target=speak_language_info, args=(language_info,)).start()
    blink_robot()

root = tk.Tk()
root.title("Dil Məlumatı App")
root.geometry("900x600")

left_frame = Frame(root, width=300, height=600, bg="white")
left_frame.pack(side="right", fill="y")

try:
    robot_img = Image.open("robot.jpg")
    robot_img = robot_img.resize((250, 350))
    robot_img = ImageTk.PhotoImage(robot_img)
except Exception as e:
    print("Robot şəkli tapılmadı:", e)
    robot_img = None

robot_label = Label(left_frame, image=robot_img, bg="white")
robot_label.pack(padx=60,pady=110)

right_frame = Frame(root, width=600, height=600, bg="white")
right_frame.pack(side="right", fill="both", expand=True)

flags = [
    ("Azerbaijan", "Azərbaycan dili", "azerbaijan.png"),
    ("Turkey", "Türk dili", "turkey.png"),
    ("England", "İngilis dili", "england.png"),
    ("France", "Fransız dili", "france.png"),
    ("Italy", "İtalyan dili", "italy.png"),
    ("Spain", "İspan dili", "spain.jpg"),
    ("Russia", "Rus dili", "russia.png")
]

flag_images = []
for idx, (country, lang, flag_file) in enumerate(flags):
    try:
        flag_img = Image.open(flag_file)
        flag_img = flag_img.resize((50, 50))
        flag_img = ImageTk.PhotoImage(flag_img)
        flag_images.append(flag_img)
    except Exception as e:
        print(f"Bayraq tapılmadı ({flag_file}):", e)
        continue

    flag_btn = Button(right_frame, image=flag_img, command=lambda c=country, l=lang: on_flag_click(c, l))
    flag_btn.grid(row=idx // 4, column=idx % 4, padx=10, pady=10)

info_label = Label(root, text="Dil haqqında məlumat", font=("Arial", 14), bg="gray", fg="white")
info_label.pack(side="bottom", fill="x")

root.mainloop()
