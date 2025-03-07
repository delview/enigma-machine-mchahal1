# TASK: Enigma Machine

# Create two functions that will accept parameters in the form of a list or dictionary that contains the str to be encrypted or decrypted
def encrypter(msg, cryptedlist):
    enlist = {
        'a':11,
        'b':12,
        'c':13,
        'd':14,
        'e':15,
        'f':21,
        'g':22,
        'h':23,
        'i':24,
        'j':24,
        'k':25,
        'l':31,
        'm':32,
        'n':33,
        'o':34,
        'p':35,
        'q':41,
        'r':42,
        's':43,
        't':44,
        'u':45,
        'v':51,
        'w':52,
        'x':53,
        'y':54,
        'z':55,
    }
    text = msg
    char_list = list(text)
    for x in char_list:
        if x in enlist:
            cryptedlist.append(enlist[x])
        else:
            print("Character not encrptable")

def decrypter(decryptlist, cryptedlist):
        delist = {
        11:'a',
        12:'b',
        13:'c',
        14:'d',
        15:'e',
        21:'f',
        22:'g',
        23:'h',
        24:'i',
        24:'j',
        25:'k',
        31:'l',
        32:'m',
        33:'n',
        34:'o',
        35:'p',
        41:'q',
        42:'r',
        43:'s',
        44:'t',
        45:'u',
        51:'v',
        52:'w',
        53:'x',
        54:'y',
        55:'z',
    }
        
        for x in decryptlist:
            if x in delist:
                cryptedlist.append(delist[x])
            else:
                print("no")
        return cryptedlist

def runagain():
    choice = input("Would you like to run again? Enter [y] or [n]: ").strip().lower()
    if choice == "y":
        mainprogram()
    if choice == "n":
         print("Bye!")
         return
    else:
         print("Enter only [y] or [n]: ")
    
# Ask user if they want to decrypt or encrypt a message
def mainprogram():
    decryptlist = []
    cryptedlist = []
    nndecryptlist = []
    code = []

    choice = input("Would you like to [e]ncrypt or [d]ecrypt a message? ").strip().lower()
    if choice == 'e':
        msg = input("Enter the message: ").strip()
    # take string and call function to encrypt or decrypt
        encrypter(msg, cryptedlist)

    # if choice == 'd':
    #     numofgroups = int(input("How many groups of numbers are there total? (e.g 21 / 33 / 51 = 3): ").strip())
    #     for i in range(numofgroups):
    #         decryptlist.append(int(input("Enter a group: ")))
    #     decrypter(decryptlist, cryptedlist)
# Test to find abetter way to enter a encryped list
    if choice == 'd':
            numofgroups = int(input("How many groups of numbers are there total? (e.g 21 / 33 / 51 = 3): "))
            code = str(input("Enter the code: ")).strip("/")
            print(code)
            nndecryptlist.append(code)
            for x in range(numofgroups):
                result = ''.join(nndecryptlist[0], nndecryptlist[1] )
                nndecryptlist.remove(nndecryptlist[0], nndecryptlist[1])
            print(result)
            decrypter(decryptlist, cryptedlist)



    # present new msg and allow user to repeat the program with that new msg
    if choice == "d":
        for i in cryptedlist:
            print(i.upper(), end = "")
            
    if choice == "e":
        for i in cryptedlist:
            print(i, "/", end = " ")

mainprogram()
31 / 15 / 12 / 42 / 34 / 33 