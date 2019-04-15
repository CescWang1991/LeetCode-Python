package grayCode

// 89. Gray Code

func grayCode(n int) []int {
	return grayCode_recursive(n)
}

// 思路：纯粹使用公式和位操作计算 第ng个格雷码为 G(n) = n XOR n/2
func grayCode_math(n int) []int {
	if n == 0 {
		return []int{0}
	}
	rlt := []int{}
	for i := 0; i < int(1<<uint(n)); i++ {
		rlt = append(rlt, i^(i>>1))
	}
	return rlt
}

// 思路：利用递归，在首位加0位或者1位
func grayCode_recursive(n int) []int {
	if n == 0 {
		return []int{0}
	}
	if n == 1 {
		return []int{0, 1}
	}
	old := grayCode_recursive(n - 1)
	// 逆序append到已有的结果中
	for i := len(old) - 1; i >= 0; i-- {
		patch := 1 << uint(n-1)
		old = append(old, patch+old[i])
	}
	return old
}
