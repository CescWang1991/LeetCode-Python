package spiralMatrixII

// 59. Spiral Matrix II

func generateMatrix(n int) [][]int {
	var rlt [][]int
	if n == 0 {
		return rlt
	}
	for i := 0; i < n; i++ {
		rlt = append(rlt, make([]int, n))
	}
	var direction int // direction should be 0(go right), 1(go down), 2(go left), 3(go up)
	top, bottom, left, right := 0, n-1, 0, n-1
	i, j := 0, 0
	for v := 1; v <= n*n; v++ {
		switch direction % 4 {
		case 0:
			rlt[i][j] = v
			if j == right {
				direction++
				top++
				i++
			} else {
				j++
			}
		case 1:
			rlt[i][j] = v
			if i == bottom {
				direction++
				right--
				j--
			} else {
				i++
			}
		case 2:
			rlt[i][j] = v
			if j == left {
				direction++
				bottom--
				i--
			} else {
				j--
			}
		case 3:
			rlt[i][j] = v
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
