from requests import get
from bs4 import BeautifulSoup as bs
import re
from os import system
from sys import argv

def help():
    print("-i install\n-s print name of tools\n-n print tools count")

def install(tool):
    try:
        system(f"sudo apt install {tool}")
    except Exception as e:
        print(f"\n{e}\n")

def pentools():
    if len(argv)>1:
        url = "https://en.kali.tools/all/"
        tools=[]
        response=get(url)
        count=re.findall(r"<p>Tool count: (\d*)</p>", str(response.text))
        print(f"total tool number ➜ {count[0]}")
        if argv[1] == "-n":
            exit()
        soup=bs(response.text, "html.parser")
        too=soup.find_all('a')
        for link in too:
            href = link.get('href')
            if type(href) == str and "?tool=" in href:
                tools.append(link.text)
        if argv[1] == "-i" : 
            for tool in tools:
                install(tool)

        elif argv[1] == "-s":
            for tool in tools:
                print(f"{tool}")
    else:
        help()
pentools()
