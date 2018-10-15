import json
from difflib import get_close_matches

data=json.load(open("data.json"))


def check(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=""
        print("Did you mean {} instead Enter Y for YES And N for NO: ".format(get_close_matches(word,data.keys())[0]))
        while(yn != "Y" or yn !="N"):
            yn=input("")
            if (yn=="Y"):
                output=data[get_close_matches(word,data.keys())[0]]
                return output
            elif (yn=="N"):
                output="No Match Found Please Double Check It"
                return output
            else:
                print("We Didn't Understand What You Entered Please ReEnter")
    else:
        return "No Match Found Please Double Check It"
def main():
    exit="Y"
    while(exit == "Y"):
        word=input("Enter The Word: ")
        output=check(word)
        if type(output)==list:
            for i in output:
                print(i)
        else:
            print(output)
        exit=input("Want To Search Again Enter Y for YES and N for NO: ")
main()
