import requests as r
from load import load
import os, sys, time
from datetime import datetime as dt
from text_func import func

def cls(): #clear command
    os.system("cls")

def help(): #from README
    print('''For the program to start working
you need to replace "null" in "settings.json"
with the necessary parameters (you can leave "emoji" as it is).
If there are problems, the program itself will report that something is wrong.
If you use the standard function, separate the words ";".

If you read this press "Enter"''')
    input()

def mods_ex(): #examples of modes

    def std(): #standart mode
        print('["text1", "text2", ...]')
        input("Enter...")

    def stairs(): #stairs mode
        print('["t", "te", "tex", "text", "tex", "te"]')
        input("Enter...")

    def running_line(): #running_line mode
        print("""['    ', '   t', '  te', ' tes', 'test', 'est', 'st', 't']
p.s.
In this version spaces will not be displayed as a discord""")
        input("Enter...")

    def wave(): #wave mode
        print("['Test', 'tEst', 'teSt', 'tesT']")
        input("Enter...")

    def r():
        print("we can't show you this")
        input("Enter...")

    while True:

        print('''Select the mod you want to see:
    1>std
    2>stairs
    3>running_line
    4>wave
    5>random
    e>exit
        ''')
        choose = input(">")

        if choose == "1":
            cls()
            std()
            cls()
            continue

        elif choose == "2":
            cls()
            stairs()
            cls()
            continue

        elif choose == "3":
            cls()
            running_line()
            cls()
            continue

        elif choose == "4":
            cls()
            wave()
            cls()
            continue

        elif choose == "5":
            cls()
            r()
            cls()
            continue

        elif choose == "e":
            cls()
            break

        else:
            cls()
            continue

def chs(): #function for select settings
    while True:
        sltime = input("Enter Interval (recommend >= 4): ")

        try:
            sltime = float(sltime)
        except ValueError:
            cls()
            print("Please use the numbers")
            continue

        print('''Select mode:
    1>standard
    2>stairs
    3>running_line
    4>wave
    5>random
''')
        choose = input(">")

        if choose == "1":
            mode = "std"

        elif choose == "2":
            mode = "stairs"

        elif choose == "3":
            mode = "running_line"

        elif choose == "4":
            mode = "wave"

        elif choose == "5":
            mode = "random"

        else:
            cls()
            continue

        return mode, sltime
        break

def main(): #"main" func
    cls()
    while True:
        print('''Select an action
    1>help
    2>mods examples
    3>start
    4>exit
    ''')
        choose = input(">")

        if choose == "1":
            cls()
            help()
            cls()
            continue

        elif choose == "2":
            cls()
            mods_ex()
            cls()
            continue

        elif choose == "3":
            cls()
            mode, sltime = chs()
            cls()
            work(mode, sltime)
            continue

        elif choose == "4":
            break

        else:
            cls()
            continue

#working func {}
def work(mode, sltime):
    try:
        rand_text = ''
        isRandom = False
        head, text, emoji, url = load()._init_(mode=mode)

        if mode == "random":
            rand_text = text
            text = "."
            isRandom = True

        while True:
            for i in text:
                if isRandom:
                    i = func().rand(rand_text)

                print("the program working")
                print("your text = '{}'".format(i))
                expires_time = dt.isoformat(dt.fromtimestamp(int(dt.timestamp(dt.utcnow())) + sltime + 3))
                payload = {'custom_status': {'text': i, 'expires_at': expires_time, "emoji_name": emoji}}
                a = r.patch(url, headers=head, json=payload)
                print(a)
                if a == '<Response [401]>':
                    print("You enter invalid AuthToken")
                time.sleep(sltime)
                cls()
    except Exception:
        print(sys.exc_info()[1])

main()
