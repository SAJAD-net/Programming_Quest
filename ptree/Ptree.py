#!/usr/bin/python3

from colorama import Fore, init
init()
import os,sys,argparse

ap=argparse.ArgumentParser()
ap.add_argument("-a","--all",nargs="?",required=False,help="show all and hiden  file or directory")
ap.add_argument("-ap","--allpath",nargs="?",required=False,help="show all and hiden  file or directory on your path")
ap.add_argument("-al","--allline",nargs="?",required=False,help="show all and hiden  file or directory and Print any thing on any line ")
ap.add_argument("-pl","--pathline",nargs="?",required=False,help="show all and hiden  file or directory")
ap.add_argument("-p","--path",nargs="?",required=False,help="path for Pstreeing in to Print any thing on any line")
ap.add_argument("-l","--line",nargs="?",required=False,help="Print any thing on any line ")
args=vars(ap.parse_args())
isfile=Fore.LIGHTRED_EX+"["+Fore.LIGHTBLUE_EX+"*"+Fore.LIGHTRED_EX+"]- "
isdir=Fore.LIGHTRED_EX+"["+Fore.LIGHTCYAN_EX+"+"+Fore.LIGHTRED_EX+"]- "
stree=[]
showed=[]
nstree=[]
def uniq(stree):
    for i in stree:
        if i not in showed:    
            showed.append(i)
            nstree.append(i)
#    print("this is the nstree -->",nstree)
def showall():
    for df in os.listdir():
        if df not in showed:
            stree.append(df)
    uniq(stree)
    for item in stree:
        if os.path.isfile(item):
            print(isfile+Fore.LIGHTBLUE_EX+item)
        elif os.path.isdir(item):
            print(isdir+Fore.LIGHTBLUE_EX+item)
def show(): 
    for df in os.listdir():
      	df=str(df)
      	if df.startswith(".") == False :
      	    stree.append(df)      
    for item in stree:
       	if os.path.isfile(item):
       	    print(isfile+Fore.LIGHTBLUE_EX+item)
       	elif os.path.isdir(item):
           print(isdir+Fore.LIGHTBLUE_EX+item)
def showoneline():
	count=0
	c=0
	items=[]
	if "-a" in sys.argv[:]:
		for df in os.listdir():
		    df=str(df)
		    if df.startswith(".") == False:			
		    	stree.append(df)
		for item in range(len(stree)):
			if os.path.isfile(item):
				print(f"{isfile+Fore.LIGHTBLUE_EX}+{stree[item]}\t{stree[item+1]}\t{stree[item+1]}")
			elif os.path.isdir(item):
				print(f"{isdir+Fore.LIGHTBLUE_EX}+{stree[item]}\t{stree[item+1]}\t{stree[item+1]}")   
		print("")

	else:
		for df in os.listdir():
			df=str(df)
			if df.startswith(".") == False :
				stree.append(df)
		for item in stree:
			if os.path.isfile(item):
				if count == 4:
					print("")
					count=0
				print(isfile+Fore.LIGHTBLUE_EX+item,end="\t")
				count+=1
			elif os.path.isdir(item):
				if count == 4:
					print("")
					count=0
				print(isfile+Fore.LIGHTBLUE_EX+item,end="\t")
				count+=1
		print("")
def geter_and_shower():
	print(Fore.LIGHTBLUE_EX+"WELCOME TO P'STREE :) ")
#--> THIS FOLOWING LINES IS THE COMMAND OF SYSTEM UNIX FOR USE
#    print(Fore.LIGHTWHITE_EX)
#    system("echo you are there --> ;pwd")
#    system("ls -1 > stree.txt")
#--> THIS FOLOWING LINE IS PYTHON CODE FOR READ LINES OF STREE.TXT FILE
#    stree[]
#    with open("stree.txt"."r") as files:
#        for line in files.readlines():
#           stree.append(i)
	count=0

	if "-a" in sys.argv[:]:
#       print("there are in the if i == '-a' ")
		print(Fore.LIGHTBLUE_EX+"you are there --> "+Fore.LIGHTGREEN_EX+os.getcwd())
		showall()
	elif "-l" in sys.argv[:]:
		print(Fore.LIGHTBLUE_EX+"you are there --> "+Fore.LIGHTGREEN_EX+os.getcwd())
		showoneline()
	elif args["allpath"]:
		os.chdir(args["allpath"])
		print(Fore.LIGHTBLUE_EX+"you are there --> "+Fore.LIGHTGREEN_EX+os.getcwd())
		showall()
	elif args["allline"]:
		print(Fore.LIGHTBLUE_EX+"you are there --> "+Fore.LIGHTGREEN_EX+os.getcwd())
		showoneline()
	elif args["pathline"]:
		os.chdir(args["pathline"])
		print(Fore.LIGHTBLUE_EX+"you are there --> "+Fore.LIGHTGREEN_EX+os.getcwd())
		showoneline()
	elif args["path"]:
#		print("there are in the if i == '-p' ")
		os.chdir(args["path"])
		print(Fore.LIGHTBLUE_EX+"you are there --> "+Fore.LIGHTGREEN_EX+os.getcwd())
		show()
	else:
#        print("there are in the else")
		show()
geter_and_shower()
