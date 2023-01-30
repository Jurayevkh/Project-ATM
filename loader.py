import time
from os import system
animation = ["Loading: 10%\n■□□□□□□□□□","Loading: 20%\n■■□□□□□□□□", "Loading: 30%\n■■■□□□□□□□", "Loading: 40%\n■■■■□□□□□□", "Loading: 50%\n■■■■■□□□□□", "Loading: 60%\n■■■■■■□□□□", "Loading: 70%\n■■■■■■■□□□", "Loading: 80%\n■■■■■■■■□□", "Loading: 90%\n■■■■■■■■■□", "Loading: 100% Welcome\n■■■■■■■■■■"]

def load():
    for i in animation:
        print(i)
        time.sleep(0.5)
        system('clear')
    print("\n")