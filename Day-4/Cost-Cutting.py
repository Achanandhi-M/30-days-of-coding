# Number of test cases
T = int(input())

# Loop through all the test cases
for i in range(1, T + 1):
    # Read the three salaries
    salaries = list(map(int, input().split()))
    
    # Sort the salaries to find the middle one
    salaries.sort()
    
    # The middle salary will be the second one after sorting
    middle_salary = salaries[1]
    
    # Output the result in the required format
    print(f"Case {i}: {middle_salary}")
