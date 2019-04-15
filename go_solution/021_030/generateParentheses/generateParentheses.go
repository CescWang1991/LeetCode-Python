package generateParentheses

import "strings"

// 022. Generate Parentheses

func generateParenthesis(n int) []string {
	return find(n, n, []string{})
}

func find(l int, r int, str []string) []string {
	if l == 0 && r == 0 {
		return []string{strings.Join(str, "")}
	}
	if l == r {
		return find(l-1, r, append(str, "("))
	} else if l > 0 {
		rlt := find(l-1, r, append(str, "("))
		rlt = append(rlt, find(l, r-1, append(str, ")"))...)
		return rlt
	} else {
		return find(l, r-1, append(str, ")"))
	}
}
