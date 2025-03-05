def encrypter(msg):
    enlist = {
        'a':11,
        'b':12,
        'c':13,
        'd':14,
    }
    text = msg
    char_list = list(text)
    for x in char_list():
        if x in enlist:
            print('yes')
        else:
            print("no")
def decrypter(msg):
    print("r")
# Ask user if they want to decrypt or encrypt a message
choice = input("Would you like to [e]ncrypt or [d]ecrypt a message? ")
msg = input("Enter the message: ")
# take string and call function to encrypt or decrypt
if choice == 'e':
    encrypter(msg)
if choice == 'd':
    decrypter(msg)
# Create two functions that will accept parameters in the form of a list or dictionary that contains the str to be encrypted or decrypted
# present new msg and allow user to repeat the program with that new msg
