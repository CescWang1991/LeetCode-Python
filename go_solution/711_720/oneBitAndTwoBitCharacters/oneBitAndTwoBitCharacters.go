package oneBitAndTwoBitCharacters

// 717. 1-bit and 2-bit Character
// 思路：遍历bits的时候根据访问的bit的值来改变遍历的步长，最后省两个或一个bit的时候判断结果
func isOneBitCharacter(bits []int) bool {
	for i:= 0; i<len(bits); {
		if len(bits)-i==1 {
			return true
		} else if len(bits)-i==2{
			if bits[i] == 1 {
				return false
			}else {
				return true
			}
		}
		if bits[i] == 0{
			i+=1
		}else {
			i+=2
		}
	}
	return true
}