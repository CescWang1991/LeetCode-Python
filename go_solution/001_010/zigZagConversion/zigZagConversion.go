package zigZagConversion
//
// 思路：找到zigZag转换的规律
func convert(s string, numRows int) string {
	if numRows <= 1 {
		return s
	}
	i, step, offset := 0, numRows+ numRows- 2, numRows+ numRows- 2
	str := []byte{}
	for i< numRows {
		count := 0
		for j:= i; j< len(s); {
			str = append(str, s[j])
			if offset <= 0 || offset == step {
				j+= step
			}else {
				if count&1 == 1 {
					j+= step- offset
				}else {
					j+= offset
				}
			}
			count++
		}
		i++
		offset -= 2
	}
	return string(str)
}