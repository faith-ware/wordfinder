from pathlib import Path
import sys

def word_find():
    try:
        theword = input("Enter an English word to get all the possible words that can be derived from it:\n").lower()
        print("-----------")
        #open and read the files as a list containing all the english words
        openFile = open(r"C:\Users\USER\Desktop\Python_practice\Read_write\words.txt")
        readFile = openFile.readlines()
        #Remove all the newlines(\n) in the list
        newFiles = "".join(readFile).lower()
        englishwords = newFiles.split("\n")
        #Turn the word to a list and get all the letters
        theLetters = list(theword)
        theDerivedwords = []

        #Get each word in the english words list
        for otherword in englishwords: 
            theLetters = list(theword)
            derivedLetters = ""
            #Get each letter in the word and compare it to the user input letters
            for eachletter in otherword:
                if eachletter in theLetters:
                    derivedLetters = derivedLetters + eachletter
                    theLetters.pop(theLetters.index(eachletter))

            if otherword == derivedLetters:      
                theDerivedwords.append(derivedLetters)
        theDerivedwords.sort(key=len,reverse=True)
        #Arrange all the derieved words according to their lenght
        for thelenght in range(len(theDerivedwords[0]),0,-1):
            print("%%%%%%%%%%%%%%%%%%%%")
            print(thelenght,"letter words")
            for b in theDerivedwords:
                if len(b) == thelenght:
                    print("  "+b)     
        openFile.close()       
        another = input("Do you want to search again? Y/N: ").lower()
        if another == "y":
            word_find()
        elif another == "n":
            sys.exit()
        word_find()     
    except Exception:
        print("Enter a word") 
        print("-----------")  
        word_find()        
word_find()        
  
        






