package lowestCommonAncestorOfABinaryTree

// 236. Lowest Common Ancestor of a Binary Tree
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// 思路：递归，在左子树和右子树中判断是否包含p或q
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	if root == p || root == q {
		return root
	}
	rlt1 := lowestCommonAncestor(root.Left, p, q)
	rlt2 := lowestCommonAncestor(root.Right, p, q)
	if rlt1 != nil && rlt2 != nil {
		return root
	} else if rlt1 != nil {
		return rlt1
	} else if rlt2 != nil {
		return rlt2
	} else {
		return nil
	}
}
