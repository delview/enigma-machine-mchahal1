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
    notcrypcount = 0
    for x in char_list:
        if x in enlist:
            cryptedlist.append(enlist[x])
        else:
            notcrypcount += 1
    
    print(f"({notcrypcount}) Character not encrptable")
    return cryptedlist

def decrypter(decryptlist, cryptedlist):
        delist = {
        11:'a', 12:'b', 13:'c', 14:'d', 15:'e',
        21:'f', 22:'g',
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
        notcrypcount = 0
        for x in decryptlist:
            if x in delist:
                cryptedlist.append(delist[x])
            else:
                notcrypcount += 1
    
        print(f"({notcrypcount}) Character were not encryptable")
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
    
#  def errorfixer(msg, choice):
#     while True:
#         try:
#             if choice == "e":
#                 if 
#                 

            
#             if choice == "d":
               
            


# Ask user if they want to decrypt or encrypt a message
def mainprogram():
    decryptlist = []
    cryptedlist = []
    code = []

    choice = input("Would you like to [e]ncrypt or [d]ecrypt a message? ").strip().lower()
    if choice == 'e':
        msg = input("Enter the message: ").strip()
    # take string and call function to encrypt or decrypt
        encrypter(msg, cryptedlist)


# asks user for the code and number of groups for decryption of the message
    if choice == 'd':
        code = input("Enter the code: ").strip()
        code = code.replace(" ", "").split("/") # remove spaces and splits the string's groups into numbers in a list
        result = ''.join(code)
        print(result)
        for groups in code:
            decryptlist.append(int(groups))
        decrypter(decryptlist, cryptedlist)

    # present new msg and allow user to repeat the program with that new msg
    if choice == "d":
        print("The decrypted message is: ")
        for i in cryptedlist:
            print(i.upper(), end = "")
        print(" ")
    if choice == "e":
        print("The encrypted message is: ")
        for i in cryptedlist:
            print(i, "/", end = " ")
        print(" ")
    runagain()

mainprogram()
31 / 15 / 12 / 42 / 34 / 33 

     