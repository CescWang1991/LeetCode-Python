package binaryTreePostorderTraversal
//
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func postorderTraversal(root *TreeNode) []int {
	return postorderIteration(root)
}

// 非递归 后续遍历
func postorderIteration(root *TreeNode) []int {
	// 需要 stack，curr(指向当前访问的节点的指针)，lastVisit(指向上一个访问的节点的指针) 来控制访问顺序
	var (
		curr = root
		stack = make([]*TreeNode, 0)
		lastVisit *TreeNode
		rlt = make([]int, 0)
	)
	for curr != nil || len(stack) != 0 {
		// 先把从curr开始所有需要访问的左子入栈
		for curr != nil {
			stack = append(stack, curr)
			curr = curr.Left
		}
		// curr 指向栈顶元素
		curr = stack[len(stack)-1]
		// 判断 curr 的右子 是否为空 或者 是否为上一个访问的节点；
		// 		如果是，说明curr可以访问，stack 出栈并访问curr 做相关更新操作
		// 		如果不是，则跳过curr，去检查curr的右子
		if curr.Right == nil || curr.Right == lastVisit {
			rlt = append(rlt, curr.Val)
			stack = stack[:len(stack)-1]
			lastVisit = curr
			curr = nil // 将已经访问过的节点置nil 为了减少内存
		}else {
			curr = curr.Right
		}
	}
	return rlt
}
// 递归 后续遍历
func postorderRecursive(root *TreeNode)[]int {
	if root == nil{
		return []int{}
	}else {
		rlt := postorderRecursive(root.Left)
		rlt = append(rlt, postorderRecursive(root.Right)...)
		rlt = append(rlt, root.Val)
		return rlt
	}
}