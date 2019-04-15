package validParentheses

// 020. Valid Parentheses
func isValid(s string) bool {
	var stack = make([]int, 0)
	for _, c := range s {
		switch c {
		case 40:
			stack = append(stack, 40)
		case 41:
			if len(stack) == 0 {
				return false
			} else if stack[len(stack)-1] != 40 {
				return false
			} else {
				stack = stack[:len(stack)-1]
			}
		case 91:
			stack = append(stack, 91)
		case 93:
			if len(stack) == 0 {
				return false
			} else if stack[len(stack)-1] != 91 {
				return false
			} else {
				stack = stack[:len(stack)-1]
			}
		case 123:
			stack = append(stack, 123)
		case 125:
			if len(stack) == 0 {
				return false
			} else if stack[len(stack)-1] != 123 {
				return false
			} else {
				stack = stack[:len(stack)-1]
			}
		default:
		}
	}
	return len(stack) == 0
}
