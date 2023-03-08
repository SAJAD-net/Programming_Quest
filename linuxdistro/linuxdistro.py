#!/usr/bin/env python3

from requests import get
from bs4 import BeautifulSoup as bs


def gets():
    url = "https://en.wikipedia.org/wiki/List_of_Linux_distributions"
    wiki = get(url)
    return wiki


def distributions():
    wiki = gets()
    soup = bs(wiki.text, "html.parser")
    tr = soup.find_all("tr")

    con, count = 1, 1
    for dis in tr:
        if count in range(287, 297):
            print(f"[{con}] ~ {dis.text}")
            print("-"*40)
            con += 1
        count += 1


distributions()
