#Sedentary_reminder

from sys import argv
from os import getpid, kill
from signal import SIGUSR1
from time import sleep
from datetime import datetime
from tkinter import messagebox
from threading import Thread
from playsound import playsound

def tkshow(label):
    now = datetime.now().strftime("%H:%m:%S")
    messagebox.showinfo( "Alarm", f"Time : {now}\n{label}")
    kill(getpid(), SIGUSR1)

def chtime(time_type, user_time):
    if time_type == "-m":
        user_time *= 60   
    elif time_type == "-h":
        user_time*=(60*60)
    return user_time

def tasks():
    if len(argv) > 3:
        time_type = argv[1]
        user_time = int(argv[2]) 
        right_time = chtime(time_type, user_time)
        label = argv[4] 
        sleep(right_time)
        Thread(target=tkshow, args=(label,)).start()
        playsound("alarm.mp3")
tasks()
