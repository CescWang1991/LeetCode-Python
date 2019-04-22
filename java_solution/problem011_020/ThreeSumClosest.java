package problem011_020;

import java.util.*;

/**
 * 016. Three Sum Closest
 * 思路同015. Three Sum
 */
public class ThreeSumClosest {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        // 指定最大的三个数之和为初始值
        int result = nums[nums.length - 3] + nums[nums.length - 2] + nums[nums.length - 1];
        for (int i = 0; i < nums.length - 1; i++){
            if(i == 0 || nums[i] > nums[i-1]) {
                int l = i + 1, r = nums.length - 1;
                while(l < r) {
                    int sum = nums[i] + nums[l] + nums[r];
                    if (Math.abs(sum - target) < Math.abs(result - target)) {
                        result = sum;
                    }
                    if (sum == target) {
                        return sum;
                    } else if (sum > target) {
                        r--;
                    } else {
                        l++;
                    }
                }
            }
        }
        return result;
    }
}
