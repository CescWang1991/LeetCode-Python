package validSudoku

// 36. Valid Sudoku
func isValidSudokuByMap(board [][]byte) bool {
	// use map to check rows, cols and areas
	var rows = map[int]map[byte]struct{}{
		0: make(map[byte]struct{}),
		1: make(map[byte]struct{}),
		2: make(map[byte]struct{}),
		3: make(map[byte]struct{}),
		4: make(map[byte]struct{}),
		5: make(map[byte]struct{}),
		6: make(map[byte]struct{}),
		7: make(map[byte]struct{}),
		8: make(map[byte]struct{}),
	}

	var cols = map[int]map[byte]struct{}{
		0: make(map[byte]struct{}),
		1: make(map[byte]struct{}),
		2: make(map[byte]struct{}),
		3: make(map[byte]struct{}),
		4: make(map[byte]struct{}),
		5: make(map[byte]struct{}),
		6: make(map[byte]struct{}),
		7: make(map[byte]struct{}),
		8: make(map[byte]struct{}),
	}
	var areas = map[int]map[byte]struct{}{
		0: make(map[byte]struct{}),
		1: make(map[byte]struct{}),
		2: make(map[byte]struct{}),
		10: make(map[byte]struct{}),
		11: make(map[byte]struct{}),
		12: make(map[byte]struct{}),
		20: make(map[byte]struct{}),
		21: make(map[byte]struct{}),
		22: make(map[byte]struct{}),
	}
	for i:= 0; i< len(board); i++ {
		for j:= 0; j< len(board); j++ {
			val := board[i][j]
			if val == '.' {
				continue
			}else {
				if _, ok := rows[i][val]; ok {
					return false
				}else {
					rows[i][val]= struct{}{}
				}
				if _, ok := cols[j][val]; ok {
					return false
				}else {
					cols[j][val]= struct{}{}
				}
				area := i/3 + 10* (j/3)
				if _, ok := areas[area][val]; ok {
					return false
				}else {
					areas[area][val]= struct{}{}
				}
			}
		}
	}
	return true
}

func isValidSudokuByBit(board [][]byte) bool {
	// use bit operations to check rows, cols and areas
	var rows, cols, areas = [9]int{}, [9]int{}, [9]int{}
	for i := range board {
		for j, v := range board[i] {
			if v == '.' {
				continue
			}
			bits := 1<< (v- '1')
			area := 3*(i/3) + (j/3)
			if bits ^ rows[i] < rows[i] || bits ^ cols[j] < cols[j] || bits ^ areas[area] < areas[area] {
				return false
			}
			rows[i] ^= bits
			cols[j] ^= bits
			areas[area] ^= bits
		}
	}
	return true
}