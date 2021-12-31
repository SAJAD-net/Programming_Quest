from random import seed, choice
from sys import argv
seed()

def make(length):
    alpha = list("abcdefghijklmnopqrstuvwxyz"\
    +"ABCDEFGHIJKLMNOPQRSTUVWXYZ"\
    +"0123456789"+"!@#$&_")
    passwd = ""
        
    for _ in range(length):
        passwd += choice(alpha)
    print(passwd)

if len(argv) > 1:
    length = int(argv[1])        
    make(length)
else:
    print("error, password length not found !")
         
        
