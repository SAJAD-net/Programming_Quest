#!/usr/bin/env python3

from random import seed, choice
from sys import argv
seed()


def make(length):
    alpha = list("abcdefghijklmnopqrstuvwxyz" +
                 "ABCDEFGHIJKLMNOPQRSTUVWXYZ" +
                 "0123456789" + "!@#$&_")

    passwd = ""

    for _ in range(length):
        passwd += choice(alpha)
    print(passwd)


if len(argv) > 1:
    LENGTH = int(argv[1])
    make(LENGTH)
else:
    print("Error, password length not found !")
    print("Usage:\n\tpython3 passcwd.py [LENGTH]")


