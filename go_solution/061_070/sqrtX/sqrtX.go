package sqrtX

// 69. Sqrt(x)
func mySqrt(x int) int {
	if x == 1 || x == 0 {
		return x
	}
	l, r := 1, x/2
	var rlt int
	for l <= r {
		mid := l + (r-l)/2
		if mid == x/mid {
			return mid
		} else if mid < x/mid {
			l = mid + 1
			rlt = mid
		} else {
			r = mid - 1
		}
	}
	return rlt
}
