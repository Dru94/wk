import sys


def Rev():
    x = input("Enter string here: ")
    s = x + " reversed is "+ x[::-1]
    return s
    

if __name__ == "__main__":
    
    print(Rev())
    
    c = input("Woould you like to reverse another word. Y or N ")
    if c.lower() == 'y':
        print(Rev())
    elif c.lower() =='n':
        sys.exit()
        
    else:
        sys.exit()