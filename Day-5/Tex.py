def changeCharacter(line, isOpeningQuote):
    # Create a list to accumulate characters (faster than concatenating strings).
    result = []
    
    # Iterate over each character in the line
    for char in line:
        if char == '"':  # If the character is a double-quote
            if isOpeningQuote:
                result.append("``")  # Replace with opening TeX-style quotes
            else:
                result.append("''")  # Replace with closing TeX-style quotes
            # Toggle the flag
            isOpeningQuote = not isOpeningQuote
        else:
            result.append(char)  # Add the character as it is if it's not a double-quote
    
    # Join the result list into a string and return it
    return ''.join(result), isOpeningQuote

def main():
    import sys
    input = sys.stdin.read 
    data = input().strip().split("\n")  
    isOpeningQuote = True
    
    for line in data:
        result, isOpeningQuote = changeCharacter(line, isOpeningQuote)
        print(result) 

if __name__ == "__main__":
    main()
