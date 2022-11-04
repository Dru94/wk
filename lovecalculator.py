import random


if __name__ == "__main__":
    player1 = list(input("Enter your full name here: ").split())
    player1Age = int(input("Enter your age here: "))
    
    player2 = list(input("Enter your partners full name here: ").split())
    player2Age = int(input("Enter your partners age here: "))
    
    love = random.randrange(20, 100)
    
    print("Your love for ", player2[0].upper(), player2[1].upper(), "is", love, "percent.")