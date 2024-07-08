import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
from PIL import Image, ImageTk
import pyttsx3
import os

root = Tk()
combobox = Combobox(root)
# combobox.pack()
root.title("Text to Speech")
root.geometry("900x450+200+200")  # Corrected geometry specification
root.resizable(False, False)
root.configure(bg='#a5a4a4')

engine = pyttsx3.init()
is_paused = False
is_stopped = True

def select_voice(gender):
    voices = engine.getProperty('voices')
    for voice in voices:
        if gender == 'Male' and 'male' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            return
        elif gender == 'Female' and 'female' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            return

def set_speech_properties(gender, speed, rate, volume, text):
    select_voice(gender)
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    if speed == "Fast":
        engine.setProperty('rate', 250)
    elif speed == 'Normal':
        engine.setProperty('rate', 150)
    else:
        engine.setProperty('rate', 60)

    engine.say(text)
    engine.runAndWait()

def speaknow():
    global is_paused, is_stopped
    text = text_area.get(1.0, END).strip()
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    rate = rate_slider.get()
    volume = volume_slider.get()

    if text:
        is_paused = False
        is_stopped = False
        set_speech_properties(gender, speed, rate, volume, text)

def pause():
    global is_paused
    if not is_paused:
        engine.stop()
        is_paused = True

def stop():
    global is_paused, is_stopped
    engine.stop()
    is_paused = False
    is_stopped = True

def replay():
    global is_paused, is_stopped
    text = text_area.get(1.0, END).strip()
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    rate = rate_slider.get()
    volume = volume_slider.get()

    if text:
        is_paused = False
        is_stopped = False
        set_speech_properties(gender, speed, rate, volume, text)

def download():
    text = text_area.get(1.0, END).strip()
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    rate = rate_slider.get()
    volume = volume_slider.get()

    if text:
        path = filedialog.askdirectory()
        if path:
            os.chdir(path)
            engine.setProperty('rate', rate)
            engine.setProperty('volume', volume)

            if speed == "Fast":
                engine.setProperty('rate', 250)
            elif speed == 'Normal':
                engine.setProperty('rate', 150)
            else:
                engine.setProperty('rate', 60)

            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

image_icon = PhotoImage(file="download.png")
root.iconphoto(False, image_icon)

Top_frame = Frame(root, bg="white", width=900, height=130)
Top_frame.place(x=0, y=0)

Logo = PhotoImage(file="new.png")
Label(Top_frame, image=Logo, bg="white").place(x=5, y=5)
Label(Top_frame, text="TEXT TO SPEECH", font="arial 30 bold", bg="white", fg="black").place(x=160, y=35)

Label(root, text="Enter your text:", font="arial 10 bold", bg="#a5a4a4", fg="black").place(x=20, y=140)

text_area = Text(root, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=15, y=170, width=400, height=260)

Label(root, text="VOICE", font="arial 13 bold", bg="#a5a4a4", fg="black").place(x=570, y=140)
Label(root, text="SPEED", font="arial 13 bold", bg="#a5a4a4", fg="black").place(x=750, y=140)

gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 13", state='readonly', width=8)
gender_combobox.place(x=560, y=170)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 13", state='readonly', width=8)
speed_combobox.place(x=740, y=170)
speed_combobox.set('Normal')

btn = Button(root, text="Speak", compound=LEFT, width=10, font="arial 10 bold", command=speaknow)
btn.place(x=450, y=220)

pause_btn = Button(root, text="Pause", compound=LEFT, width=10, font="arial 10 bold", command=pause)
pause_btn.place(x=590, y=380)

stop_btn = Button(root, text="Stop", compound=LEFT, width=10, font="arial 10 bold", command=stop)
stop_btn.place(x=690, y=380)

replay_btn = Button(root, text="Replay", compound=LEFT, width=10, font="arial 10 bold", command=replay)
replay_btn.place(x=790, y=380)

save = Button(root, text="Download", compound=LEFT, width=10, bg="#39c790", font="arial 10 bold", command=download)
save.place(x=450, y=260)      

# Adding sliders for rate, volume, and pitch
Label(root, text="Rate", font="arial 13 bold", bg="#a5a4a4", fg="black").place(x=570, y=220)
rate_slider = Scale(root, from_=50, to_=300, orient=HORIZONTAL, font="arial 10", length=200)
rate_slider.set(150)
rate_slider.place(x=650, y=220)

Label(root, text="Volume", font="arial 13 bold", bg="#a5a4a4", fg="black").place(x=570, y=260)
volume_slider = Scale(root, from_=0, to_=1, resolution=0.1, orient=HORIZONTAL, font="arial 10", length=200)
volume_slider.set(1.0)
volume_slider.place(x=650, y=260)

Label(root, text="Pitch", font="arial 13 bold", bg="#a5a4a4", fg="black").place(x=570, y=300)
pitch_slider = Scale(root, from_=50, to_=300, orient=HORIZONTAL, font="arial 10", length=200)
pitch_slider.set(150)
pitch_slider.place(x=650, y=300)

root.mainloop()
