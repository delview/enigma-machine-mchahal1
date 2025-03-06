def encrypter(msg):
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
            print(enlist[x])
        else:
            print("no")

def decrypter(decryptlist):
        delist = {
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
        
        for x in decryptlist:
            if x in delist.values():
                print(delist[x])
            else:
                print("no")
# Ask user if they want to decrypt or encrypt a message
decryptlist = []
choice = input("Would you like to [e]ncrypt or [d]ecrypt a message? ")
if choice == 'e':
    msg = input("Enter the message: ")
# take string and call function to encrypt or decrypt
    encrypter(msg)
if choice == 'd':
    numofgroups = int(input("How many groups of numbers are there?"))
    for i in range(numofgroups):
        decryptlist.append(input("Type a group: "))
    decrypter(decryptlist)
# Create two functions that will accept parameters in the form of a list or dictionary that contains the str to be encrypted or decrypted
# present new msg and allow user to repeat the program with that new msg
