import sys

def CountWords():
    x = input("Enter your text here: ")
    ls = list(x.split(" "))
    print("Text has {} words.".format(len(ls)))
    
    
if __name__ == "__main__":
    CountWords()
    sys.exit()