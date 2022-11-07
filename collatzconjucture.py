import sys

def Collatz(number):
    n=0
    while number > 1:
        if number % 2 == 0:
            n = n/2
        else:
            n = (3*n) +1
            
        return n


if __name__ == "__main__":
    y = input("Enter a number here: ")
    print(Collatz(y))
    
    sys.exit()