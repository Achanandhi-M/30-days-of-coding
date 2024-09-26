def process_equation(equation):
    return equation


def main():
    import sys
    input=sys.stdin.read
    data=input().strip().split("\n")
    for line in data:
        result=process_equation(line.strip())
        print(result)
    
    
if __name__ == "__main__":
    main()