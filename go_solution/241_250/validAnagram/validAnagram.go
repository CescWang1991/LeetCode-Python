package validAnagram

/* 242. Valid Anagram
Input: s = "anagram", t = "nagaram"
Output: true
*/
func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	count := make([]uint8, 26)

	for index, _ := range count {
		count[index] = 0
	}

	for i := 0; i < len(s); i++ {
		count[s[i]-97]++
		count[t[i]-97]--
	}

	for _, val := range count {
		if val != 0 {
			return false
		}
	}
	return true
}
