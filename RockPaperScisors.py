import random
from time import sleep
from os import system, name

Movements = ["Rock", "Paper", "Scissors"]
r = "Rock"
p = "Paper"
s = "Scissors"
uc = ""
cc = ""
win = """ █████   █████  ███            █████                                 
░░███   ░░███  ░░░            ░░███                                  
 ░███    ░███  ████   ██████  ███████    ██████  ████████  █████ ████
 ░███    ░███ ░░███  ███░░███░░░███░    ███░░███░░███░░███░░███ ░███ 
 ░░███   ███   ░███ ░███ ░░░   ░███    ░███ ░███ ░███ ░░░  ░███ ░███ 
  ░░░█████░    ░███ ░███  ███  ░███ ███░███ ░███ ░███      ░███ ░███ 
    ░░███      █████░░██████   ░░█████ ░░██████  █████     ░░███████ 
     ░░░      ░░░░░  ░░░░░░     ░░░░░   ░░░░░░  ░░░░░       ░░░░░███ 
                                                            ███ ░███ 
                                                           ░░██████  
                                                            ░░░░░░   """
draw = """ ██████████                                      
░░███░░░░███                                     
 ░███   ░░███ ████████   ██████   █████ ███ █████
 ░███    ░███░░███░░███ ░░░░░███ ░░███ ░███░░███ 
 ░███    ░███ ░███ ░░░   ███████  ░███ ░███ ░███ 
 ░███    ███  ░███      ███░░███  ░░███████████  
 ██████████   █████    ░░████████  ░░████░████   
░░░░░░░░░░   ░░░░░      ░░░░░░░░    ░░░░ ░░░░    
                                                 
                                                 
                                                 """
lose = """ ██████████               ██████                      █████   
░░███░░░░███             ███░░███                    ░░███    
 ░███   ░░███  ██████   ░███ ░░░   ██████   ██████   ███████  
 ░███    ░███ ███░░███ ███████    ███░░███ ░░░░░███ ░░░███░   
 ░███    ░███░███████ ░░░███░    ░███████   ███████   ░███    
 ░███    ███ ░███░░░    ░███     ░███░░░   ███░░███   ░███ ███
 ██████████  ░░██████   █████    ░░██████ ░░████████  ░░█████ 
░░░░░░░░░░    ░░░░░░   ░░░░░      ░░░░░░   ░░░░░░░░    ░░░░░  
                                                              
                                                              
                                                              """

def slowType(msg, nl=False):
    for i in msg:
        print(i, end="", flush=True)
        sleep(.08)
    if nl != False:
        print()
        
def clear():
    system("cls" if name == "nt" else "clear")

def computer():
    cc = random.choice(Movements)
    return cc


def user():
    slowType("Chose one input to play from this: ", True)
    print("Rock,    Paper,  Scissors.")
    slowType("Eter your answer: ")
    uc = input()
    uc = uc.lower()
    if uc == "r" or uc == "rock":
        uc = "Rock"
    elif uc == "p" or uc == "paper":
        uc = "Paper"
    elif uc == "s" or uc == "scissors":
        uc = "Scissors"
    else:
        user()
    return uc

def main():
    clear()
    cc = computer()
    uc = user()
    if cc == uc:
        clear()
        print(f"You: {uc}               ", end="")
        sleep(3)
        print(f"Computer: {cc}")
        print("\n\n" + draw)
        input("Press enter to exit...")
    elif cc == r and uc == p:
        clear()
        print(f"You: {uc}               ", end="")
        sleep(3)
        print(f"Computer: {cc}")
        print("\n\n" + win)
        input("Press enter to exit...")
    elif cc == r and uc == s:
        clear()
        print(f"You: {uc}               ", end="")
        sleep(3)
        print(f"Computer: {cc}")
        print("\n\n" + lose)
        input("Press enter to exit...")
    elif cc == p and uc == r:
        clear()
        print(f"You: {uc}               ", end="")
        sleep(3)
        print(f"Computer: {cc}")
        print("\n\n" + lose)
        input("Press enter to exit...")
    elif cc == p and uc == s:
        clear()
        print(f"You: {uc}               ", end="")
        sleep(3)
        print(f"Computer: {cc}")
        print("\n\n" + win)
        input("Press enter to exit...")
    elif cc == s and uc == r:
        clear()
        print(f"You: {uc}               ", end="")
        sleep(3)
        print(f"Computer: {cc}")
        print("\n\n" + win)
        input("Press enter to exit...")
    elif cc == s and uc == p:
        clear()
        print(f"You: {uc}               ", end="")
        sleep(3)
        print(f"Computer: {cc}")
        print("\n\n" + lose)
        input("Press enter to exit...")
    

if __name__ == "__main__":
    main()

