#Define our alphabet with every uppercase letter
DICTIONARY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#caesar encryption and decryption fucntion
# @params mode : (encrypt, decrypt) , key : String , message : String
def caesar(mode, key, message):
    #Make an iterator which repeats indefinitely key values
    message = message.replace(" ","")
    k = DICTIONARY[key]
    text = []
    #Itarate over message string
    #We read one character at a time
    for i in message:
         pos1 = DICTIONARY.index(i.upper())
         pos2 = DICTIONARY.index(k.upper())
         if(mode == "encrypt"):
             l = (pos1 + pos2) % 26
         elif(mode == "decrypt"):
             l = (pos1 - pos2) % 26

         text.append(DICTIONARY[l])

    return ''.join(text)

if __name__ == "__main__":
    mode = "encrypt"
    key = 3
    message = input('What is your message?')#
    print(vigenere(mode, key, message))
    mode = "decrypt"
    message = "PHHWPHDIWHUWKHWRJDSDUWB"
    print(vigenere(mode, key, message))
