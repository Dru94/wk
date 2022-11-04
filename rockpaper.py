import sys
import random

def play(pick):
    selection = ['rock', 'paper', 'scissors']
    
    p = pick.lower()
    _choice = random.choice(selection)
    print(p, " VS ",_choice)
    
    if p == "rock" and _choice == "paper":
        print("Paper Wraps Rock. Paper Wins")
        
    elif p == "rock" and _choice == "scissors":
        print("Rock crushes scissors. You Win.")
        
    elif p == "paper" and _choice == "rock":
        print("Paper Wraps Rock. You Win.")
        
    elif p == "paper" and _choice == "scissors":
        print("Scissors Cut Paper. Scissors Win.")
        
    elif p == "scissors" and _choice == "rock":
        print("Rock Crushes Scissors. Rock Wins.")
        
    elif p == "scissors" and _choice == "paper":
        print("Scissors Cut Paper. You Win.")
    elif p == _choice:
        print("ITS A DRAW")
    else:
        print("Something went wrong")
        sys.exit()
        

if __name__ == "__main__":
    x = input("Rock Paper Scissors. Enter your selection: ")

    play(x)
    sys.exit()
    