package binaryTreePreorderTraversal

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func preorderTraversal(root *TreeNode) []int {
	return preorderInteration(root)
}
// 非递归 前序遍历
func preorderInteration(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	var (
		// 利用 stack 来存储需要需要访问的节点
		stack = []*TreeNode{root}
		rlt   = make([]int, 0)
	)
	for len(stack) != 0 {
		// 出栈，直接访问
		curr := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		rlt = append(rlt, curr.Val)
		// 先将右子入栈，在将左子入栈
		if curr.Right != nil {
			stack = append(stack, curr.Right)
		}
		if curr.Left != nil {
			stack = append(stack, curr.Left)
		}
	}
	return rlt
}

// 递归 前序遍历
func preorderRecursive(root *TreeNode) []int {
	if root == nil {
		return []int{}
	} else {
		rlt := []int{root.Val}
		rlt = append(rlt, preorderRecursive(root.Left)...)
		rlt = append(rlt, preorderRecursive(root.Right)...)
		return rlt
	}
}
