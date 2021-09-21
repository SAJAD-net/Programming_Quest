from sys import argv

alpha = "abcdefghijklmnopqrstuvwxyz"
chars = list(alpha)

def encryptor(key, plain):
    cipher = ""
    
    for ch in plain:
        ind = alpha.index(ch.lower())
        dex = lambda x:x*key%26 if ind != 0 else 0
        nc = chars[dex(ind)]
        cipher+=nc
    print(cipher)

def decryptor(key, cipher):
    plain = ""

    def rever(key):
        for n in range(100):
            if n*key%26 == 1:
                return n

    rev = rever(key) 
    for ch in cipher:
        ind = alpha.index(ch.lower())
        dex = lambda x:x*rev%26 if x != 0 else 0
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
