import random
import sys
   
    

if __name__ == "__main__":
    words = ['hangman', 'man', 'hang', 'candy', 'oesophagus', 'movie', 'music', 'eat', 'journalist', 'headphones']
    
    _chosen = random.choice(words)
    dashes = ['_' for i in range(0,len(_chosen))]
    chances = 0
    print("Guess this", len(_chosen), "letter word.")
    
    while "_" in dashes:
        guess = input("Enter letter here: ")
        if guess in _chosen:
            dashes[_chosen.index(guess)] = guess
            _chosen = _chosen.replace(guess, "*", 1)
        else:
            print("Wrong guess try again.")

        finalStr = "".join(dashes)
        print("Progress: ", finalStr)
        chances+=1
    
    print("You have used", chances ,"chances to guess the", len(_chosen), "letter word.")
    
    sys.exit()