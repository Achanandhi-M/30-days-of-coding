def happyBirthday(n, names):
    # Define the lyrics of the birthday song
    lyrics = [
        "Happy", "birthday", "to", "you",
        "Happy", "birthday", "to", "you",
        "Happy", "birthday", "to", "Rujia",
        "Happy", "birthday", "to", "you"
    ]

    total_lines = len(lyrics)
    # Calculate how many times to repeat the lyrics
    repeats = (n + total_lines - 1) // total_lines  # Number of full repetitions needed
    for i in range(total_lines * repeats):
        singer_index = i % n  # Determine which singer's turn it is
        print(f"{names[singer_index]}: {lyrics[i % total_lines]}")  # Print the name with the corresponding lyric

def main():
    import sys
    input = sys.stdin.read  # Read input from standard input
    data = input().strip().split("\n")  # Split input into lines
    n = int(data[0])  # The first line contains the number of names
    names = [data[i] for i in range(1, n + 1)]  # Extract the names
    happyBirthday(n, names)  # Call the happyBirthday function

if __name__ == "__main__":
    main()
