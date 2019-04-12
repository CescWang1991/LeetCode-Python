package spiralMatrix

// 54. Spiral Matrix
func spiralOrder(matrix [][]int) []int {
	if len(matrix) == 0 {
		return []int{}
	}
	var direction int // direction should be 0(go right), 1(go down), 2(go left), 3(go up)
	total := len(matrix) * len(matrix[0])
	top, bottom, left, right := 0, len(matrix)-1, 0, len(matrix[0])-1
	var rlt []int
	i, j := 0, 0
	for v := 0; v < total; v++ {
		switch direction % 4 {
		case 0:
			rlt = append(rlt, matrix[i][j])
			println(right)
			if j == right {
				direction++
				top++
				i++
			} else {
				j++
			}
		case 1:
			rlt = append(rlt, matrix[i][j])
			if i == bottom {
				direction++
				right--
				j--
			} else {
				i++
			}
		case 2:
			rlt = append(rlt, matrix[i][j])
			if j == left {
				direction++
				bottom--
				i--
			} else {
				j--
			}
		case 3:
			rlt = append(rlt, matrix[i][j])
			if i == top {
				direction++
				left++
				j++
			} else {
				i--
			}
		}
	}
	return rlt
}
