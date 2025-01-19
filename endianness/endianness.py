#!/usr/bin/env python3

 
in_word = input("- Enter a string to get both [Little Endian/Big Endian]: ")
big_endian = ""
little_endian = ""

for i in range(len(in_word)):
    big_endian += hex(ord(in_word[i]))
    little_endian += hex(ord(in_word[-(i+1)]))

big_endian = big_endian.replace("0x", "")
little_endian = little_endian.replace("0x", "")
print(f"LE : {little_endian}\nBE : {big_endian}")
