def generateAnswer(value): 
    answer= (value*567) // 9
    answer1=(answer+7492)*235
    answer2=(answer1//47) - 498
    answer_int = abs(int(answer2))
    #return (abs((((((value * 567) // 9) + 7492) * 235) // 47) - 498) // 10) % 10
    tens_digit = (answer_int // 10) % 10 
    return tens_digit
def main():
    import sys
    input=sys.stdin.read
    data=input().strip().split("\n")
    t=int(data[0])
    for i in range(1,t+1):
     value = int(data[i])  # Extract the value for each test case
     result=generateAnswer(value)
     print(result)
        
if __name__=="__main__":
    main()
    
