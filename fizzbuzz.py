import sys

def fizzbuzz(target):
    for i in range(1, target+1):
        if i%3 == 0:
            print("fizz")
        elif i%5 == 0:
            print("buzz")
        else:
            print(i)

if __name__ == "__main__":
    x = int(input("Enter fizzbuzz target: "))
    
    print(fizzbuzz(x))
    
    sys.exit()