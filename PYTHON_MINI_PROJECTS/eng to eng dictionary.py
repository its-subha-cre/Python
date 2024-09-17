
import json
import difflib as d

j=json.load(open("data.json"))

def translate(w):
    if w in j.keys():
         print(j[w])
    elif d.get_close_matches(w,j.keys()):
        print(f"did you mean this {d.get_close_matches(w,j.keys())[0]}")
        print(f"then the word meaning is {j[d.get_close_matches(w,j.keys())[0]]}")
    else:
        print("the word is not found")

# print(translate('ca'))
word=input("enter a word:")
translate(word)

