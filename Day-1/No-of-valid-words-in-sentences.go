package main

import (
	"fmt"
	"regexp"
	"strings"
)

// Function to check if a token is valid
func isValidWord(token string) bool {
	// Define the regular expression pattern
	pattern := `^[a-z]+(-[a-z]+)?[.!?,]?$`
	// Compile the regular expression
	regex := regexp.MustCompile(pattern)
	// Check if the token matches the pattern
	return regex.MatchString(token)
}

// Function to count valid words in a sentence
func countValidWords(sentence string) int {
	// Split the sentence into words based on spaces
	words := strings.Fields(sentence)
	count := 0

	for _, word := range words {
		if isValidWord(word) {
			count++
		}
	}

	return count
}

func main() {
	// Test cases
	fmt.Println(countValidWords("cat and  dog"))                            // Output: 3
	fmt.Println(countValidWords("!this  1-s b8d!"))                         // Output: 0
	fmt.Println(countValidWords("alice and  bob are playing stone-game10")) // Output: 5
}
