package multiplyStrings

import "bytes"

// 043. Multiply Strings
func multiply(num1 string, num2 string) string {
	if len(num1) == 1 && num1 == "0" {
		return "0"
	} else if len(num2) == 1 && num2 == "0" {
		return "0"
	}
	dic := map[int]string{
		0: "0",
		1: "1",
		2: "2",
		3: "3",
		4: "4",
		5: "5",
		6: "6",
		7: "7",
		8: "8",
		9: "9",
	}
	slot := make([]int, len(num1)+len(num2))
	for idx1 := len(num1) - 1; idx1 >= 0; idx1-- {
		for idx2 := len(num2) - 1; idx2 >= 0; idx2-- {
			posHi := idx1 + idx2
			posLo := posHi + 1
			val := int((num1[idx1]-'0')*(num2[idx2]-'0')) + slot[posLo]
			slot[posLo] = val % 10
			slot[posHi] = (slot[posHi]*10 + val) / 10
		}
	}
	buf := bytes.Buffer{}
	numDetected := false
	for _, v := range slot {
		if v == 0 && !numDetected {
			continue
		}
		numDetected = true
		buf.WriteString(dic[v])
	}
	return buf.String()
}
