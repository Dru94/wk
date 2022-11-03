import sys

def ageToSeconds(age):
    ans = age * 31536000
    
    return ans

if __name__ == "__main__":
    age = int(input("Enter your age here: "))
    
    print("You have lived for", ageToSeconds(age), "seconds.")
    sys.exit()
    