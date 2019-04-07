package reverseInteger
// 7. Reverse Integer
func reverse(x int) int {
	max := 1<<31 -1
	min := -1* 1<<31
	if x < min || x > max {
		return 0
	}else if x < 10 && x >-10{
		return x
	}
	rlt := 0
	for x != 0 {
		var b int
		x, b = x/10, x%10
		rlt = 10*rlt + b
		if rlt < min || rlt > max {
			return 0
		}
	}
	return rlt
}