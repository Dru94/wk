import time
import itertools
import sys


def names(fNames, sNames):
    names = list(itertools.product(sNames, fNames))
    print("NOTE: ",len(names), "possible name combination/s were found.")
    
    time.sleep(3)
    
    for _ in names:
        name = _[0] +" "+ _[1] 
        print(name)

if __name__ == "__main__":
    surNames = list(map(str,input("Enter one or more Surnames e.g Kabuye Kivumbi Kaliisa: ").split()))
    
    firstNames = list(map(str,input("Enter one or more Firstnames e.g Andrew David John: ").split()))
    
    
    names(firstNames, surNames)
    
    print("***EXITING***")
    
    sys.exit()
    
    
    
    

        
 

    

    