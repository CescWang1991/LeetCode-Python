package intergerToRoman

import "strings"
//
// 思路：构造合适的静态数据，方便查找和构造结果
func intToRoman(num int) string {
	var M []string = []string{"", "M", "MM", "MMM"}
	var C []string = []string{"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"}
	var X []string = []string{"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"}
	var I []string = []string{"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"}
	sb := strings.Builder{}
	sb.WriteString(M[num/1000])
	sb.WriteString(C[(num%1000)/100])
	sb.WriteString(X[(num%100)/10])
	sb.WriteString(I[num%10])
	return sb.String()
}
