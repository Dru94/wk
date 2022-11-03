import sys


def celciusToFarenheit(number):
    ans = (number * 1.8) + 32
    ans = str(ans) + "\N{DEGREE SIGN}" + "c"
    return ans

def farenheitToCelcius(number):
    ans = (number-32) * 5/9
    
    ans = str(ans) + "\N{DEGREE SIGN}" + "f"
    return ans


if __name__ == "__main__":
    conversion = input("Enter F for Celcius to Farenheit or C for Farenheit to Celcius degree: ")
    
    conversion = conversion.lower()
    
    if conversion == "f":
        deg = int(input("Enter degrees in Celcius here: "))
        print(celciusToFarenheit(deg))
        sys.exit()
        
    elif conversion == "c":
        deg = int(input("Enter degrees in Farenheit here: "))
        print(farenheitToCelcius(deg))
        sys.exit()
    else:
        print("Wrong input")
        sys.exit()