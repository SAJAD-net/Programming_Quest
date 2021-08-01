#!/usr/bin/python3

import os
from pyfiglet import figlet_format
from colorama import Fore
import argparse
ap=argparse.ArgumentParser()
ap.add_argument("-t","--text",required=True,help="text to figleting")
ap.add_argument("-c","--color",required=False,help="color to figleting")
args=vars(ap.parse_args())
def figlet():
        try:
            text = args["text"]
            color=Fore.BLUE
            if args["color"]:
                color=args["color"]
                if color == 'red':
                    color=Fore.LIGHTRED_EX
                elif color == 'blue':
                    color=Fore.BLUE
                elif color == 'black':
                    color = Fore.LIGHTBLACK_EX
                elif color == 'cyan':
                    color = Fore.CYAN
                elif color == 'green':
                    color = Fore.GREEN
            print(color,figlet_format(text))
        except Exception as e:
            print(Fore.LIGHTRED_EX+"Err not found ! --> %s"%e)
figlet()
