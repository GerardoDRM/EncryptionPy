from collections import OrderedDict
from itertools import product
import re
import numpy as np

DICTIONARY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def check_key(key):
    #Check repeated values in the key
    return "".join(OrderedDict.fromkeys(key)).upper()

def generateMatrix(key):
    if ('J' in key or 'I' in key):
        newDict = re.sub('[IJ]','',DICTIONARY)
    else:
        newDict = re.sub('J','',DICTIONARY)

    matrixValues = "".join(OrderedDict.fromkeys(key + newDict))
    #Slide string values and generate a numpy array
    matrix = np.array([list(matrixValues[i:i+5]) for i in range(0, len(matrixValues),5)])
    print(matrix,'\n')
    return matrix

def transform_message(message):
    message = message.replace(' ','')
    return [message[i:i+2] for i in range(0, len(message),2)]

def repeatedLetters(message):
    group = transform_message(message)
    for idx, i in enumerate(group):
        if(re.search(r'((\w)\2)',i)):
             group[idx] = i[:1] + 'X' +i[1:]
             return repeatedLetters(''.join(group))
        if(len(i) == 1):
            group[idx] = i + 'X'
    return group

def genCartesianProduct(matrix):
    dic = {}
    #2. If both letters fall in the same row
    for row in matrix:
        for i, j in product(range(5), repeat=2):
            if i != j:
                dic[row[i] + row[j]] = row[(i + 1) % 5] + row[(j + 1) % 5]
    #3. If both letters fall in the same column
    for c in zip(*matrix):
        for i, j in product(range(5), repeat=2):
            if i != j:
                dic[c[i] + c[j]] = c[(i + 1) % 5] + c[(j + 1) % 5]
    #4. Cross-connection
    for i1, j1, i2, j2 in product(range(5), repeat=4):
        if i1 != i2 and j1 != j2:
            dic[matrix[i1][j1] + matrix[i2][j2]] = matrix[i1][j2] + matrix[i2][j1]
    return dic

def translate(message, matrix, mode):
    #1. If a pair is a repeated letter
    group = repeatedLetters(message)
    # Generate all possible combinatios
    cartesianP = genCartesianProduct(matrix)
    if(mode == 'decrypt'):
        cartesianP = dict((v, k) for k, v in cartesianP.items())
    elif(mode != 'decrypt' and mode != 'encrypt'):
        return "Invalid Mode"

    for idx, i in enumerate(group):
        group[idx] = cartesianP[i]
    return ''.join(group)

def playfair(key, message, mode):
    newKey = check_key(key)
    print("KEY --> " + newKey + "\n")
    #Create playfair matrix
    matrix = generateMatrix(newKey)
    #Translate maessage
    print("MESSSAGE --> "+translate(message,matrix,mode))

if __name__ == "__main__":
    key = "LARGEST"
    messageE = "MUST SEE YOU OVER CADOGAN WEST COMING AT ONCE"
    modeE = "encrypt"
    playfair(key, messageE, modeE)
    messageD = "UZTBDLGZPNNWLGTGTUEROVLDBDUHFPERHWQSRZ"
    modeD = "decrypt"
    playfair(key, messageD, modeD)
