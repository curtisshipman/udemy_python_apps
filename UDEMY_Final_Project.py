#!/usr/bin/env python3
# Import needed modules globally

import os
import re
import time
import fileinput
import operator
import sys

##########################################
'''

this needs to be handled.  it breaks if you pass a bad file name at the command line.

'''
def get_file():
    # Gets the file to be parsed
    if len(sys.argv) > 1:
        try:
            fileName = sys.argv[1]
            openFile = open(fileName,  "r", encoding="utf8")
            openFile1 = openFile.read()
            fileName = os.path.basename(fileName)
            (fileName, ext) = os.path.splitext(fileName)
            openFile.close
        except FileNotFoundError:
            print("That file does not exist.  Please use a valid file name.")
            return
    else:
        x = False
        while x == False:
            try:
                fileName = input("What file shall we parse?\nPlease enter filename, including extension: ")
                openFile = open(fileName,  "r", encoding="utf8")
                openFile1 = openFile.read()
                fileName = os.path.basename(fileName)
                (fileName, ext) = os.path.splitext(fileName)
                openFile.close
                x = True
            except FileNotFoundError:
                print("Please use a valid file name.")
                x = False
    return openFile1, fileName

def fake_processing():
    # This is just a dumb joke.  Off by default.
    # This can be turned on in the main function if you like.
    i = 0
    print("Processing.  Please Stand By.")
    while i < 7:
        if i < 4:    
            print("\r.",)
            time.sleep(1)
            i+=1
        elif i < 6:
            print("Processing..."), time.sleep(2)
            i+=1
        else:
            print("Maybe now..."), time.sleep(3), print("Almost..."), time.sleep(1), print("Hold on..."), time.sleep(2), print("Got it!")
            i+=1
            print("Installing Virus...      "), time.sleep(.5)
            print("[DONE]")
            print("\nComputer is now compromised!"), time.sleep(1.5)
            print("\nRelax!  It's just a joke!\n")

def stringToList(string):
    # Converts a string to a list
    listRes = list(string.split(" "))
    return listRes

def make_dict(listFile):
    # Converts a list to a dictionary
    # Counts the totals time a key value exists in the original list
    dictFile = {}
    for word in listFile:
        if word.lower() in dictFile:
            dictFile[word.lower()] +=1
        else:
            dictFile[word.lower()] = 1
    return dictFile

def remove_character(openFile1):
    # Removes all the non-aplphnumeric charachters
    string1 = re.sub('[^A-Za-z0-9]+',' ', openFile1)
    return string1

def make_output_file(inputFile, dictFile1, fileName):
    # Generates the output file
    outFile = open("{}-output.txt".format(fileName), "w", encoding="utf8")
    outFile.write("Total Words  -  {}\nUnique Words  -  {}\n\n".format(len(inputFile.split()), len(dictFile1)))
    sorted_dictFile1 = sorted(dictFile1.items(), key=operator.itemgetter(1), reverse=True)
    for wordinfo in sorted_dictFile1:
        outFile.write("{}  -  {}\n".format(wordinfo[0], wordinfo[1]))
    outFile.close()

def main():
    # Main function to call other functions
    full_path = os.path.realpath(__file__)
    path, filename = os.path.split(full_path)
    os.chdir(path)
    inputFile, fileName = get_file()
    noSymbolsFile = remove_character(inputFile)
    filteredFile = noSymbolsFile.split()
    dictFile1 = make_dict(filteredFile)
    make_output_file(noSymbolsFile, dictFile1, fileName)
    #fake_processing()
    print("Your new file has been generated.\n")
    print("Your new file location is {}.\nHave a nice day!".format(os.getcwd()))
    print("{}-output.txt".format(fileName))
    print("Your new file location is {}\{}-output.txt".format(os.getcwd(), fileName))

if __name__ == "__main__":
    main()
