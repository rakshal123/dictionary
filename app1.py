import json
import difflib
from difflib import *

data=json.load(open("C:/Users/Rahul Dwivedi/Downloads/data.json"))
def translate(word):
    try:
        for i in data[word]:
            print(i)
    except KeyError:
        print("wrong word selection!Run the program again")
        word=input("Enter word again: ")
        translate(word)


word=input("Enter the word: ")
word=word.lower()
w=get_close_matches(word,data.keys())
print(w[0])
translate(str(w[0]))
