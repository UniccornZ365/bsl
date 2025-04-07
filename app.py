from flask import Flask,redirect
from flask import render_template
from os import listdir
from os.path import isfile, join
import random
import os

#to run this:
#  flask  --debug run 

app = Flask(__name__)

def getFileList():
    onlyfiles = [f for f in listdir("data") if isfile(join("data", f))]
    strippedList = []
    for file in onlyfiles:
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
        if currentFileName != "everything.txt" and currentFileName != "words.txt" and currentFileName !="places.txt":
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

if __name__ == "__main__":
    app.run(debug=True)