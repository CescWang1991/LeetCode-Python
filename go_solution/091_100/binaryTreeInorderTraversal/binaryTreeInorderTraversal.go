package binaryTreeInorderTraversal

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderTraversal(root *TreeNode) []int {
	return inorderIteration(root)
}
// 非递归 中序遍历
// 思路：先将从curr开始把所有可以到达的左子入栈
// 		然后curr=stack.Pop()，并将curr指向自己的右子，再从curr开始把所有可以到达的左子入栈然后再消费栈顶
func inorderIteration(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	var (
		// 需要 stack 和一个 curr指针 来控制访问的顺序
		stack = []*TreeNode{}
		curr  = root
		rlt   = make([]int, 0)
	)
	for curr != nil || len(stack) != 0 {
		// 先把从curr开始所有需要访问的左子入栈
		for curr != nil {
			stack = append(stack, curr)
			curr = curr.Left
		}
		// 出栈并访问
		curr = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		rlt = append(rlt, curr.Val)
		// curr 指向右子
		curr = curr.Right
	}
	return rlt
}

// 递归 中序遍历
func inorderRecurive(root *TreeNode) []int {
	if root != nil {
		rlt := inorderRecurive(root.Left)
		rlt = append(rlt, root.Val)
		return append(rlt, inorderRecurive(root.Right)...)
	} else {
		return []int{}
	}
}
