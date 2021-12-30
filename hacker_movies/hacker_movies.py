from requests import get
from bs4 import BeautifulSoup as bs


def action():
    site = "https://www.purevpn.com/blog/list-of-hacker-and-cybersecurity-movies/"
    headers = { "referer" : "google.com"}
    resp = get(site, headers=headers)
    print(resp.text)
    soup = bs(resp.text, "html.parser")
    names = soup.find_all("a")
    print(names)
    for name in names:
        print(name)

action()
