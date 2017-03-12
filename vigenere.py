from itertools import cycle

#Define our alphabet with every uppercase letter
DICTIONARY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Get the plain or encrypted text from file
# @return text : String
def getText():
    text = open("text.txt","r").read()
    text = text.replace(" ","")
    return text.replace("\n","")

#Vigenere encryption and decryption fucntion
# @params mode : (encrypt, decrypt) , key : String , message : String
def vigenere(mode, key, message):
    #Make an iterator which repeats indefinitely key values
    message = message.replace(" ","")
    k = cycle(list(key))
    text = []
    #Itarate over message string
    #We read one character at a time
    for i in message:
         pos1 = DICTIONARY.index(i.upper())
         pos2 = DICTIONARY.index(k.__next__().upper())
         if(mode == "encrypt"):
             l = (pos1 + pos2) % 26
         elif(mode == "decrypt"):
             l = (pos1 - pos2) % 26

         text.append(DICTIONARY[l])

    return ''.join(text)

if __name__ == "__main__":
    mode = "encrypt"
    key = "ABCD"
    message = input('What is your message?')
    print(vigenere(mode, key, message))
    mode = "decrypt"
    message = "LPN"
    print(vigenere(mode, key, message))
