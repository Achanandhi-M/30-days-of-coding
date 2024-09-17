package main

import (
	"fmt"
	"strings"
)

func countWord(sentence string) {

	wordCount := make(map[string]int)
	words := strings.Split(sentence, "")

	for _, word := range words { // _, denotes indexes
		wordCount[word]++
	}

	for word, count := range wordCount {
		fmt.Println("No of times word occured", word, ":", count)
	}
}

/*
func main() {
	sentence := "bananaorange"
	countWord(sentence)
}
*/
