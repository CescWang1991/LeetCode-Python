package twoSum
// 1. Two Sum
func twoSum(nums []int, target int) []int {
	trace := make(map[int]int)
	for idx, v := range nums {
		if k, ok := trace[target-v]; ok {
			return []int{k, idx}
		}
		if _, ok := trace[v]; !ok {
			trace[v] = idx
		}
	}
	return []int{}
}
