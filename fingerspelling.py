import random

def fingerSpellingFiles():
    #Declaring the list variables
    fileList = []
    possibleWords = []
    letters = []

    #Making a list of words to choose from in upper case
    wordFile = open(r"words.txt", "r")
    for line in wordFile:
        possibleWords.append(line.upper().rstrip())

    #Choosing a random word from the list
    wordNum = random.randint(0,len(possibleWords)-1)
    word = possibleWords[wordNum]

    #Turing the string into a list of characters and adding them to letters as the file which corresponds to the letter
    for character in word:
        letters.append(f"/static/letters/{character}.svg")

    print(letters)

    #At end return list of files to show
    return letters, word
