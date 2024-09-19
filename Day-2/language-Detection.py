def detectLanguage(language):
    
    greetings = {
        "HELLO": "ENGLISH",
        "HOLA": "SPANISH",
        "HALLO": "GERMAN",
        "BONJOUR": "FRENCH",
        "CIAO": "ITALIAN",
        "ZDRAVSTVUJTE": "RUSSIAN"
    }
    
    return greetings.get(language, "UNKNOWN")

def main():
    
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    case_number = 1
    
    for line in data:
        line = line.strip()
        if line == "#":
            break
        result = detectLanguage(line)
        print(f"Case {case_number}:  {result}")
        case_number += 1

if __name__ == "__main__":
    main()
