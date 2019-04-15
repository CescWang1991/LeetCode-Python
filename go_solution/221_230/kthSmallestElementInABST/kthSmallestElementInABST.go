package kthSmallestElementInABST

// 230. Kth Smallest Element in a BST

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func kthSmallest(root *TreeNode, k int) int {
	// use inorder iteration
	if root == nil {
		return -1
	}
	stack := []*TreeNode{}
	curr := root
	for len(stack) != 0 || curr != nil {
		for curr != nil {
			stack = append(stack, curr)
			curr = curr.Left
		}
		curr, stack = stack[len(stack)-1], stack[:len(stack)-1]
		k--
		if k == 0 {
			return curr.Val
		}
		curr = curr.Right
	}
	return -1
}
