from requests import get
from bs4 import BeautifulSoup as bs
from sys import argv

def weather():
    url = "https://www.accuweather.com/en/ir/iran-weather/"
    headers = {"user-agent" : "Mozila/95", "refere":"google.com"}
    res = get(url, headers=headers)
    soup = bs(res.text, "html.parser")
    wh = soup.find_all('a',attrs={'class':'nearby-location weather-card'})
    c = 1
    if len(argv) > 2 and argv[1] == "-s":
        state = argv[2].capitalize()
        for a in wh:    
            if state in a.text:
                print(a.text.strip())
                break
            c+=1
    else:   
        for a in wh:    
            print(f"{a.text.strip()}\n", "-"*20)
            

weather()
