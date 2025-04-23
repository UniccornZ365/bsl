from flask import Flask,redirect
from flask import render_template

import os
from os import listdir
from os.path import isfile, join

import random

from fingerspelling import fingerSpellingFiles

#to run this:
#  flask  --debug run 

app = Flask(__name__)

def getFileList():
    onlyfiles = [f for f in listdir("data") if isfile(join("data", f))]
    strippedList = []
    for file in onlyfiles:
        if file.count(".txt"):
            filestripped = file.replace(".txt","")
            if filestripped.count("-") > 0:
                filestripped = filestripped.replace("-","")
            strippedList.append(filestripped.title())
    return strippedList


def getRandom(category):

    possibleWords = []
    
    f = open(join("data",f"{category.lower()}.txt"), "r")
    possibleWords = f.readlines()
    f.close()

    word = possibleWords[random.randint(0,(len(possibleWords)-1))].title()

    return word



@app.route("/random/everything")
def everything():
    file_to_delete = open(join("data","everything.txt"),'w')
    file_to_delete.close()
    #directory = [file for file in os.listdir("data") if file != "everything.txt"]
    for currentFileName in (os.listdir("data")):
        if currentFileName != "everything.txt" and currentFileName != "words.txt" and currentFileName !="places.txt" and currentFileName.count(".txt") > 0 :
            currentFile =open(join("data",currentFileName),"r")
            currentFileLines = currentFile.readlines()
            for words in currentFileLines:
                with open(join("data","everything.txt"), "a") as myfile:
                    myfile.write(words)

            with open(join("data","everything.txt"), "a") as myfile:
                    myfile.write("\n")        
        else:
            continue


    strippedList = getFileList()

    category = "everything"
    word = getRandom(category) 
    return render_template("page.html", requested = category, chosenword = word.strip('\n'), files=strippedList)


@app.route("/random/<category>")
def random_word_by_category(category):
       

    #List Files for Menu
    strippedList = getFileList()

    #Find Word if Exists
    file_path = join("data",f"{category.lower()}.txt")
    if os.path.exists(file_path):
        word = getRandom(category) 
        return render_template("page.html", requested = category, chosenword = word.strip('\n'), files=strippedList)
    else:
        return render_template("notExist.html", requested = category, files=strippedList)
    
@app.route("/api/random/<category>")
def random_word_by_category_api(category):
    word = getRandom(category) 
    return {
        "chosenword": word
    }

@app.route("/random")
def randompage():
    return redirect("/random/everything", code=302)

@app.route("/about")
def about():
    strippedList = getFileList()
    return render_template("about.html",files=strippedList)

@app.route("/")
def home():
    return redirect("/about", code=302)

#Finger Spelling Game

@app.route("/fingerspelling")
def fingerspelling():
    strippedList = getFileList()
    fingerFiles, word = fingerSpellingFiles()

    return render_template("fingerspelling.html", files=strippedList, fingerfiles = fingerFiles, word=word)

@app.route("/api/fingerspelling")
def fingerspelling_data():
    fingerFiles, word = fingerSpellingFiles()
    return{
        "word":word,
        "fingerfiles":fingerFiles
    }

@app.route("/quiz")
def test():
    strippedList = getFileList()
    return render_template("quiz.html",files = strippedList)

@app.errorhandler(404)
def page_not_found(e):
    strippedList = getFileList()  # Pass the file list for the menu if needed
    return render_template("error.html", files=strippedList), 404


if __name__ == "__main__":
    app.run(debug=True)

