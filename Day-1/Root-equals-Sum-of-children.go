package main

//import "fmt"

//Definition for a binary tree node.

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func checkTree(root *TreeNode) bool {
	if root.Val == root.Left.Val+root.Right.Val {
		return true
	}
	return false
}

/*
func main() {
	// Example tree
	root := &TreeNode{
		Val:   10,
		Left:  &TreeNode{Val: 3},
		Right: &TreeNode{Val: 6},
	}
	result := checkTree(root)
	fmt.Println(result)
}
*/
