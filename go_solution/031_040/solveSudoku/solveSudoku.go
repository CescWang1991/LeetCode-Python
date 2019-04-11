package solveSudoku

func solveSudoku(board [][]byte) {
	solve(board)
}

// 最朴素的递归，没有用剪枝进行优化
func solve(board [][]byte) bool {
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board); j++ {
			if board[i][j] != '.' {
				continue
			}
			for v := '1'; v <= '9'; v++ {
				if ok := isValid(board, i, j, byte(v)); !ok {
					continue
				}
				board[i][j] = byte(v)
				if ok := solve(board); ok {
					return true
				} else {
					board[i][j] = '.'
				}
			}
			return false
		}
	}
	return true
}

// 利用位操作来判断 行， 列， 块 是否可以填入目标数字
func isValid(board [][]byte, r, c int, val byte) bool {
	var row, col, area = 0, 0, 0
	// 构造目标行的数据
	for _, v := range board[r] {
		if v == '.' {
			continue
		}
		row ^= 1 << (v - '1')
	}
	// 构造目标列的数据
	for i := 0; i < len(board); i++ {
		if board[i][c] == '.' {
			continue
		}
		col ^= 1 << (board[i][c] - '1')
	}
	// 构造目标块的数据
	for i := 3 * (r / 3); i < 3*(r/3)+3; i++ {
		for j := 3 * (c / 3); j < 3*(c/3)+3; j++ {
			if board[i][j] == '.' {
				continue
			}
			area ^= 1 << (board[i][j] - '1')
		}
	}
	bits := 1 << (val - '1')
	// 如果 bits^row < row 说明 bits 和 rows 在某一位上都位1 造成冲突
	if bits^row < row || bits^col < col || bits^area < area {
		return false
	}
	return true
}
