import random
import time
import sys


def magic():
    qn = input("Enter your question here: ")
    
    if qn == "" or qn == " " or qn == None:
        return "I Can't be of any help to you then."
    
    print("hmmm...")
    
    answers = [
        'It is certain', 'It is decidedly so', 'Without a doubt', 
        'Yes – definitely', 'You may rely on it', 'As I see it, yes', 
        'Most likely', 'Outlook good', 'Yes Signs point to yes', 
        'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now',
        'Cannot predict now', 'Concentrate and ask again', 'Dont count on it',
        'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful'
        ]
    
    
    return random.choice(answers)

def Replay(c):
    if c.lower() == "y":
        magic()
    else:
        sys,exit()


if __name__=="__main__":
    print("Welcome, how may I be of service ? Call me the Magic 8 Ball.")
    time.sleep(2)
    print(magic())
    print("Hope that helps.")
    time.sleep(2)
    aqn = input("Do you have another question. Y or N : ")
    
    if aqn.lower() == "y":
        Replay(aqn)
    elif aqn.lower() == "n":
        sys.exit()
    else:
        print("Unknown input.")
        sys.exit()
        
        