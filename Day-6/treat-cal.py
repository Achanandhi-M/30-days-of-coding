def main():
    case_number = 1
    
    while True:
        N = int(input().strip())
        if N == 0:
            break
        
        events = list(map(int, input().strip().split()))
        reasons_count = 0
        treats_count = 0
        
        for event in events:
            if event == 0:
                treats_count += 1
            elif 1 <= event <= 99:
                reasons_count += 1
        
        # Calculate Emoogle Balance
        emoogle_balance = reasons_count - treats_count
        
        # Output the result
        print(f"Case {case_number}: {emoogle_balance}")
        case_number += 1

if __name__ == "__main__":
    main()
