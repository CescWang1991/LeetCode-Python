package problem011_020;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

/**
 * 018. Four Sum
 * 双指针做法，三层循环，时间复杂度为O(n^3)
 */
public class FourSum {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        HashSet<List<Integer>> set = new HashSet<>();   // 设置hashset用来去重
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 3; i++) {
            for (int j = i+1; j < nums.length - 2; j++) {
                int lo = j + 1, hi = nums.length - 1;
                while (lo < hi) {
                    int sum = nums[i] + nums[j] + nums[lo] + nums[hi];
                    if (sum == target) {
                        List<Integer> temp = new ArrayList<>();
                        temp.add(nums[i]);
                        temp.add(nums[j]);
                        temp.add(nums[lo]);
                        temp.add(nums[hi]);

                        if (!set.contains(temp)) {
                            set.add(temp);
                            result.add(temp);
                        }
                        lo ++;
                        hi --;
                    } else if (sum < target) {
                        lo ++;
                    } else {
                        hi --;
                    }
                }
            }
        }
        return result;
    }
}
