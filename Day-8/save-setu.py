def donate(balance,value):
    balance+=value
    return balance


def report(balance):
    return balance

def main():
    import sys
    input=sys.stdin.read
    data=input().strip().split("\n")
    balance=0
    t=int(data[0])
    for i in range(1,t+1):
     command = data[i].split()
     if command[0]=="donate":
         value=int(command[1])
         balance=donate(balance,value)
     elif command[0]=="report":
         print(report(balance))
     else:
         print("Invalid choice")
        
if __name__=="__main__":
    main()
    