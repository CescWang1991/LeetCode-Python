package uniquePaths

import "testing"

type TestCase struct {
	m int
	n int
	expect int
}

func Test_uniquePaths(t *testing.T) {

	tcs := []TestCase{
		{3,2,3},
		{7,3,28},
	}
	for _, tc := range tcs {
		out := uniquePaths(tc.m, tc.n)
		if tc.expect != out {
			t.Logf("m: %v, n: %v, expect: %v got: %v", tc.m, tc.n, tc.expect, out)
		}
	}
}
