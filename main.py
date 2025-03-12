# TASK: Enigma Machine

# Create two functions that will accept parameters in the form of a list or dictionary that contains the str to be encrypted or decrypted
def encrypter(msg, cryptedlist):
    enlist = {
        'a':11, 'b':12, 'c':13, 'd':14, 'e':15,
        'f':21, 'g':22, 'h':23, 'j':24, 'k':25,
        'l':31, 'm':32, 'n':33, 'o':34, 'p':35,
        'q':41, 'r':42, 's':43, 't':44, 'u':45,
        'v':51, 'w':52, 'x':53, 'y':54, 'z':55,
    }
    text = msg.lower() # copys inputed msg into "text"
    char_list = list(text) # changes text into a list
    notcrypcount = 0
    for x in char_list: # loops for every ltter in the user inputed message
        if x in enlist: # checks if each letter is in the dictionary
            cryptedlist.append(enlist[x]) # adds the corresponding number to cryptedlist
        else:
            notcrypcount += 1 # counts the num of characters that were not encryptable
    
    print(f"({notcrypcount}) Character(s) were not encryptable")
    return cryptedlist # returns the encrypted list

def decrypter(decryptlist, cryptedlist):
        delist = {
        11:'a', 12:'b', 13:'c', 14:'d', 15:'e',
        21:'f', 22:'g', 23:'h', 24:'j', 25:'k',
        31:'l', 32:'m', 33:'n', 34:'o', 35:'p', 
        41:'q', 42:'r', 43:'s', 44:'t', 45:'u',
        51:'v', 52:'w', 53:'x', 54:'y', 55:'z',
    }
        notcrypcount = 0
        for x in decryptlist: # loops for however many groups are in decryplist
            if x in delist: # checks if the gorup is in the dictionary
                cryptedlist.append(delist[x]) # adds the corresponding letter to cryptedlist
            else:
                notcrypcount += 1 # counts if the chacter was unable to be transformed
    
        print(f"({notcrypcount}) Character(s) were not encryptable")
        return cryptedlist # returns the crypted list

def runagain():
    while True:
        choice = input("Would you like to run again? Enter [y] or [n]: ").strip().lower()
        if choice == "y":
            mainprogram()
        if choice == "n":
            break
        else:
            print("Enter only [y] or [n]: ")
    print("Bye!")
    
# Ask user if they want to decrypt or encrypt a message
def mainprogram():
    decryptlist = []
    cryptedlist = []
    code = []
    while True: # main loop to check if the user inputed e or d
        choice = input("Would you like to [e]ncrypt or [d]ecrypt a message? ").strip().lower()
        if choice == 'e': # e to encrypt a normal message
            msg = input("Enter the message: ").strip()
        # take string and call function to encrypt or decrypt
            encrypter(msg, cryptedlist)


    # asks user for the code and number of groups for decryption of the message
        if choice == 'd': # to decrypt a coded message
            while True: # loop to check if user inputed a correcttly formatted cipher
                try:
                    code = input("Enter the code: ").strip()
                    code = code.replace(" ", "").split("/") # remove spaces and splits the code into groups by / 
                    for groups in code: # loops for however many "groups" are in the list
                            decryptlist.append(int(groups)) # changes the "groups into integers and addes it to a to be decrypt list"
                    decrypter(decryptlist, cryptedlist)
                    break
                except ValueError:
                    print("Enter a proper Polybius Square Cipher! e.g (31 / 15 / 12 / 42 / 34 / 33)")
                    continue
                break
        
        # present new msg and allow user to repeat the program with that new msg
        if choice == "d":
            print("NOTE: I's are changed into J's due to the Polybius Square Cipher.")
            print("The decrypted message is: ")
            for i in cryptedlist: # prints each letter in crypted list to make the final result
                print(i.upper(), end = "")
            print(" ")
            break
        if choice == "e":
            print("The encrypted message is: ")
            for i in cryptedlist: # prints each number in the list along with a /
                print(i, "/", end = " ")
            print(" ")
            break
        else:
            print("Enter only [e] to encrypt a message or [d] to decrypt a message.")
    runagain() # asks to run the program again

mainprogram()
31 / 15 / 12 / 42 / 34 / 33 

     