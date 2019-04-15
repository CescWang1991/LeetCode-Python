package reverseInteger
// 7. Reverse Integer
func reverse(x int) int {
	max := 1<<31 -1 // max val for int and int32
	min := -1* 1<<31 // min val for int and int32
	if x < min || x > max {
		return 0
	}else if x < 10 && x > -10{
		return x // not need to reverse
	}
	rlt := 0
	for x != 0 {
		var remain int
		x, remain = x/10, x%10
		rlt = 10*rlt + remain
		if rlt < min || rlt > max {
			return 0
		}
	}
	return rlt
}