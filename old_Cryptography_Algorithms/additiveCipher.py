from sys import argv

alpha = "abcdefghijklmnopqrstuvwxyz"
chars = list(alpha)

def encryptor(key, plain):
    cipher=""
    for ch in plain:
        ind = alpha.index(ch.lower())
        dex = lambda x:x+key-26 if x+key >= 26 else x+key
        nc = chars[dex(ind)]
        cipher+=nc
    print(cipher)

def decryptor(key, cipher):
    plain=""
    for ch in cipher:
        ind = alpha.index(ch.lower())
        dex = lambda x:x-key+26 if x-key < 0 else x-key
        nc = chars[dex(ind)]
        plain+=nc
    print(plain)

if len(argv) > 3:
    key = int(argv[2])
    if argv[1] == "-e":
        plain = argv[3]
        encryptor(key, plain)
    elif argv[1] == "-d":
        cipher = argv[3]
        decryptor(key, cipher)        
