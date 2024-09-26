def detectName(line):
    name={
        "Hajj":"Hajj-e-Akbar",
        "Umrah":"Hajj-e-Asghar"
    }
    return name.get(line)


def main():
    
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    case_number = 1
    
    for line in data:
        line = line.strip()
        if line == "*":
            break
        result = detectName(line)
        print(f"Case {case_number}: {result}")
        case_number += 1

if __name__ == "__main__":
    main()




