def detectNumber(L, W, H):
    # Fixed dimensions of the suitcase
    max_size = 20
    
    # Check if the box fits in the suitcase for any orientation
    if (L <= max_size and W <= max_size and H <= max_size):
        return True
    if (L <= max_size and H <= max_size and W <= max_size):
        return True
    if (W <= max_size and H <= max_size and L <= max_size):
        return True
    return False

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    # Read the number of test cases
    T = int(data[0])
    
    results = []
    for i in range(1, T + 1):
        # Read dimensions L, W, H
        L, W, H = map(int, data[i].split())
        
        # Check if the box fits in any orientation
        if detectNumber(L, W, H):
            results.append(f"Case {i}: good")
        else:
            results.append(f"Case {i}: bad")
    
    # Print all results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
