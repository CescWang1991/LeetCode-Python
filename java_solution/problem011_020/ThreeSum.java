package problem011_020;

import java.util.*;

/**
 * 015. Three Sum
 * 将数组nums先排序，然后循环内部做双指针遍历。
 */
public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < nums.length - 1; i++) {
            if(i == 0 || nums[i] > nums[i-1]) {     // 判断nums[i-1]和nums[i]是否重复，若重复直接跳过
                int l = i + 1, r = nums.length - 1;
                while (l < r) {
                    int sum = nums[i] + nums[l] + nums[r];
                    if (sum == 0) {
                        result.add(Arrays.asList(nums[i], nums[l], nums[r]));
                        l++;
                        r--;
                        while (l < r && nums[l] == nums[l-1]) { // 检验重复值，若重复则直接跳过
                            l++;
                        }
                        while (l < r && nums[r] == nums[r+1]) {
                            r--;
                        }
                    } else if (sum > 0) {
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
