from flask import Flask,redirect
from flask import render_template
from os import listdir
from os.path import isfile, join
import random
import os

#to run this:
#  flask  --debug run 

app = Flask(__name__)

def getRandom(category):

    possibleWords = []
    
    f = open(join("data",f"{category.lower()}.txt"), "r")
    possibleWords = f.readlines()
    f.close()

    word = possibleWords[random.randint(0,(len(possibleWords)-1))]

    return word

@app.route("/random")
def home():
    return redirect("/random/everything", code=302)


@app.route("/random/<category>")
def random_word_by_category(category):
       

    #List Files for Menu
    onlyfiles = [f for f in listdir("data") if isfile(join("data", f))]
    strippedList = []
    for file in onlyfiles:
        filestripped = file.replace(".txt","")
        strippedList.append(filestripped.title())

    #Find Word if Exists
    file_path = join("data",f"{category.lower()}.txt")
    if os.path.exists(file_path):
        word = getRandom(category) 
        return render_template("page.html", requested = category, chosenword = word.replace(' ','-').strip('\n'), files=strippedList)
    else:
        return render_template("notExist.html", requested = category, files=strippedList)
    
@app.route("/api/random/<category>")
def random_word_by_category_api(category):
    word = getRandom(category) 
    return {
        "chosenword": word
    }

@app.route("/about")
def about():
    onlyfiles = [f for f in listdir("data") if isfile(join("data", f))]
    strippedList = []
    for file in onlyfiles:
        filestripped = file.replace(".txt","")
        strippedList.append(filestripped.title())
    return render_template("about.html",files=strippedList)

if __name__ == "__main__":
    app.run(debug=True)