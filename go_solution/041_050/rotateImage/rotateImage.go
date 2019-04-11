package rotateImage

// 思路：按顺时针交换对应位置上的元素
func rotate_solution1(matrix [][]int)  {
	// switch element in clockwise order
	s := len(matrix) -1
	for i:=0;i<len(matrix)/2;i++ {
		for j:= i; j<s-i;j++ {
			matrix[i][j],matrix[j][s-i],matrix[s-i][s-j],matrix[s-j][i] =
				matrix[s-j][i],matrix[i][j],matrix[j][s-i],matrix[s-i][s-j]
		}
	}
}

// 思路：先上下翻转 + 再对角线翻转 = 顺时针转动
func rotate_solution2(matrix [][]int)  {
	s := len(matrix)-1
	// 先上下翻转
	for i:= 0 ; i<len(matrix)/2; i++ {
		matrix[i], matrix[s-i] = matrix[s-i], matrix[i]
	}
	// 再对角线翻转
	for i:= 0 ; i<len(matrix); i++ {
		for j:= i+1; j< len(matrix); j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}
}