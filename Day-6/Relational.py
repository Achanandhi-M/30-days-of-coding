def detectRelation(value1,value2):
    if value1 > value2:
        return '>'
    elif value1 == value2:
        return '='
    else:
        return '<'


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    t=int(data[0])
    for i in range(1,t+1):
        value1,value2=map(int,data[i].split())
        result=detectRelation(value1,value2)
        print(result)

if __name__ == "__main__":
    main()