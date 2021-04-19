import os, zipfile
import sys

def killer(path):
        
        print("[!]--> starting ...")
        file=zipfile.ZipFile(path,"r")
        os.mkdir("./password-Killer")
        with open("source/.dicts","rb") as dicts:
                for pwd in dicts.readlines():
                        try:
                                Efile=file.extractall("./password-Killer",pwd=pwd.strip())
                                print("[+] the password of file is ==>",pwd)
                                print("[!]--> finished !")
                                break
                        except:
                                pass
                file.close()


def run():
        os.system("clear") if os.name == "posix" else os.system("cls")
        if len(sys.argv) > 1:
            path = sys.argv[1]
            killer(path)
        else:
            path=input("[!]--> enter path of file --> > ").strip()
            killer(path) 
run()
