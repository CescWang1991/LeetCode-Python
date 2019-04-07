package validSudoku

import "testing"

func Test_isValidSudoku(t *testing.T) {

	var board [][]byte = [][]byte{
		[]byte(".87654321"),
		[]byte("2........"),
		[]byte("3........"),
		[]byte("4........"),
		[]byte("5........"),
		[]byte("6........"),
		[]byte("7........"),
		[]byte("8........"),
		[]byte("9........"),
	}
	t.Log(isValidSudokuByBit(board))
}
