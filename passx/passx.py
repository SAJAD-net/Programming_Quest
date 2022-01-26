import os, zipfile
import sys

def killer(path, dictfile):
    print("[!] starting ...")
    file=zipfile.ZipFile(path,"r")
    os.mkdir("passx")
    with open(dictfile, "rb") as dicts:
        for pwd in dicts.readlines():
            try:
                Efile=file.extractall("./passx/", pwd.strip())
                print(f"[+]  password : {pwd}")
                print("[!]  finished !")
                break
            except:
                pass
    file.close()

def run():
    if len(sys.argv) > 2:
        path = sys.argv[1]
        dictfile = sys.argv[2]
        killer(path, dictfile)
    else:
        print("usage : python3 passx.py [PATH] [DICTIONARY]")
run()
