from sys import argv
from bs4 import BeautifulSoup as bs
from requests import get
from prettytable import PrettyTable


url = "https://www.accuweather.com/en/ir/iran-weather/"
headers = {"user-agent" : "Mozila/95", "refere":"google.com"}
table = PrettyTable(["City", "Degree(celsius)"])


def weather(specific_city):
    res = get(url, headers=headers)
    soup = bs(res.text, "html.parser")
    wh = soup.find_all('a',attrs={'class':'nearby-location weather-card'})

    for a in wh:    
        info = a.text.split("\n")
        if specific_city:
            if specific_city in info:
                table.add_row([info[1], info[3]])
                break
        else:
            table.add_row([info[1], info[3]])

    print(table)


if len(argv) > 2 and argv[1] == "-c":
    specific_city = argv[2].capitalize()
elif len(argv) > 1 and argv[1] == '-a':
    specific_city = None
else:
    print("""Usage : python3 weather.py [OPTIONS]\n\
            OPTIONS:\t-a : to get all cities\n\
            \t\t-c [CITY] : to get a specific city\n""")
    exit()


weather(specific_city)
