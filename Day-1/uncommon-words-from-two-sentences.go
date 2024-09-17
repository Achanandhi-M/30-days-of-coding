/*
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order

*/

package main

import (
	"fmt"
	"strings"
)

func uncommonFromSentences(s1 string, s2 string) []string {
	wordCount := make(map[string]int)

	word1 := strings.Split(s1, " ")
	word2 := strings.Split(s2, " ")

	for _, word := range word1 {
		wordCount[word]++
	}

	for _, word := range word2 {
		wordCount[word]++
	}
	fmt.Println("Map value:", wordCount)

	var result []string
	for word, count := range wordCount {
		if count == 1 {
			result = append(result, word)
		}
	}
	return result
}

/*func main() {
	// Example sentences
	s1 := "apple banana pineapple"
	s2 := "banana orange"

	// Get uncommon words
	result := uncommonFromSentences(s1, s2)
	fmt.Println(result) // Output: [orange apple]
}*/
