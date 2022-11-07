import random

def PasswordGenerator():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    symbols = "!@#"
    
    password = ""
    
    s = random.choices(letters, k=5)
    for letter in s:
        password += str(ord(letter))+random.choice(letters)+random.choice(symbols)
    
    password = password[:9]
    
    print("Generated Password: ",password)

if __name__=="__main__":
   PasswordGenerator()