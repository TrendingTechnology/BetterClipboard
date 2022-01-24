import clipboard
import json
import time
import os
from os import path

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

SAVE = "save.json"


def loader():
    with open(SAVE, "r") as f:
        return json.load(f)

if not path.exists(SAVE):
    with open(SAVE, "w") as f:
        json.dump({"count":0}, f)
else:
    ans = input("Would you like to reset your saved clipboards? (Y/n)\n.: ")
    if ans.lower() == "y" or ans.lower() == "yes":
        count = 0
        with open(SAVE, "w") as f:
            json.dump({"count":0}, f)
    else:
        data = loader()
        count = int(data["count"])

def saver(data):
    with open(SAVE, "w") as f:
        json.dump(data, f)

def paster():
    global count
    data = loader()
    count += 1
    data[str(count)] = clipboard.paste()
    data["count"] = count
    saver(data)
    print("\nContent from your clipboard has been saved. ")
    time.sleep(2)
    printer()
    ask()

def copy(key):
    data = loader()
    try:
        clipboard.copy(data[key])
        print("\nContent has been pasted into your clipboard. ")
        time.sleep(2)
        printer()
        ask()
    except:
        print("\nInvalid ID, please make sure to select a valid one. \n")
        ask()

    printer()
    ask()


def printer():
    cls()
    data = loader()
    for entry in data:
        if not entry == "count":
            print(f"""----------------------------------------------------------------
                                                                       
        {entry}.                                                          
            {data[entry]}                                                         
                                                                                   """)

def ask():
    to_copy = input("----------------------------------------------------------------\n\n\n>>> Type an ID to paste to clipboard \nTo save something instead, type SAVE .: ")

    if to_copy.lower() != "save":
        copy(to_copy)
    else:
        paster()

printer()
ask()