if __name__ == "__main__":
    text = input("Enter text here: ")
    
    text = list(text)
    text.reverse()
    
    print("Reversed text is: ", "".join(text))