package searchInRotatedSortedArray

// 33. Search in Rotated Sorted Array
// 思路：除了比较 nums[mid] 和 target 来决定如何移动 l 和 r，还要判断 nums[mid] 和 target 是不是在同一边
func search(nums []int, target int) int {
	if len(nums) == 0 {
		return -1
	}
	l, r := 0, len(nums)-1
	for l <= r {
		mid := (l + r) / 2
		if target == nums[mid] {
			return mid
		}
		if nums[l] <= nums[mid] {
			if nums[l] <= target && target <= nums[mid] {
				r = mid - 1
			} else {
				l = mid + 1
			}
		} else {
			if target >= nums[mid] && target <= nums[r] {
				l = mid + 1
			} else {
				l = mid - 1
			}
		}
	}
	return -1
}
