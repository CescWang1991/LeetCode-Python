package solveSudoku

import "testing"

func Test_Set(t *testing.T) {
	var board [][]byte = [][]byte{
		[]byte("53..7...."),
		[]byte("6..195..."),
		[]byte(".98....6."),
		[]byte("8...6...3"),
		[]byte("4..8.3..1"),
		[]byte("7...2...6"),
		[]byte(".6....28."),
		[]byte("...419..5"),
		[]byte("....8..79"),
	}
	solveSudoku(board)
	for _, v := range board {
		t.Log(string(v))
	}
}
func Test_isValid(t *testing.T)  {
	var board [][]byte = [][]byte{
		[]byte("53..7...."),
		[]byte("6..195..."),
		[]byte(".98....6."),
		[]byte("8...6...3"),
		[]byte("4..8.3..1"),
		[]byte("7...2...6"),
		[]byte(".6....28."),
		[]byte("...419..5"),
		[]byte("....8..79"),
	}
	t.Log(isValid(board, 0,6, '6'))
}

