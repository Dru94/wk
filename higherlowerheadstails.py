import time
import random
import sys

def higherLower(number, target):
    if number > target:
        print("Higher")
    elif number < target:
        print("Lower")        
    else:
        print("CORRECT. TARGET FOUND")
        sys.exit()
        
        
def headsTails():
    num = random.randint(1, 500)
    num = num // 3 
    if num % 2 == 0:

        return "Heads Wins."
    else:

        return "Tails Wins."
    
    

if __name__ == "__main__":
    game = input("Enter 1 to play Higer or Lower. Enter 2 to play Heads or Tails: ")
    
    if game == "1":
        print("You selected Higher or Lower.\nYou have 15 chances to guess the target number between 1 to 100.")
        time.sleep(1)
        target = random.randint(1,100)
        i = 0
        while i < 15:
            guess = int(input("Enter your guess here: "))
            higherLower(guess, target)
            i+=1
        print("You have used up your chances. The Target value is", target)
        
        sys.exit()
        
    elif game == "2":
       print("You seleted heads or tails.")
       time.sleep(1)
       
       side = input("Enter H for heads or T for tails: ")
       side = side.lower()
       
       if side == "h":
           print(headsTails())
           sys.exit()
       elif side == "t":
           print(headsTails())
           sys.exit()
       else:
           print("***Wrong Input***")
           sys.exit()
