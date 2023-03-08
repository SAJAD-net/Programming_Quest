#!/usr/bin/env python3


import argparse
import sys
from os import getpid, kill
from signal import SIGUSR1
from time import sleep
from datetime import datetime
from tkinter import messagebox
from threading import Thread
from playsound import playsound


def tkshow(label):
    """ Displays a simple tkinter window """

    now = datetime.now().strftime("%H:%m:%S")
    messagebox.showinfo("Alarm", f"Time : {now}\n{label}")
    kill(getpid(), SIGUSR1)


def chtime(time_type, delay):
    """ Calculates the delay time """

    if time_type == "m":
        delay *= 60
    elif time_type == "h":
        delay *= (60 * 60)
    return delay


# Initialize the command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--minute", help="one minute")
ap.add_argument("-H", "--hour", help="one hour")
ap.add_argument("-l", "--label", help="label")

args = vars(ap.parse_args())


def main():
    if len(args) == 3:
        if delay := args["minute"]:
            time_type = "m"
        elif delay := args["hour"]:
            time_type = "h"
        if args["label"]:
            label = args["label"]
        else:
            ap.print_help()
            sys.exit()

        fin_time = chtime(time_type, int(delay))
        sleep(fin_time)
        Thread(target=tkshow, args=(label,)).start()
        playsound("alarm.mp3")

    else:
        ap.print_help()
        sys.exit()


main()
