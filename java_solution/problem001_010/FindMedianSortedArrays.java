package problem001_010;

/**
 * 004. Median of Two Sorted Arrays
 */
public class FindMedianSortedArrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int length = nums1.length + nums2.length;
        if (length %2 == 0) {
            return ((double)findKthElem(nums1, nums2, 0, 0, length/2) + (double)findKthElem(nums1, nums2, 0, 0, length/2+1))/2;
        } else {
            return findKthElem(nums1, nums2, 0, 0, (length+1)/2);
        }
    }

    private int findKthElem(int[] nums1, int[] nums2, int s1, int s2, int k) {
        int m = nums1.length;
        int n = nums2.length;
        if (s1 >= m) {
            return nums2[s2 + k - 1];
        }
        if (s2 >= n) {
            return nums1[s1 + k - 1];
        }
        if (k == 1) {
            return Math.min(nums1[s1], nums2[s2]);
        }

        int mid = Math.floorDiv(k, 2) - 1;
        int k1 = s1 + mid >= m? Integer.MAX_VALUE: nums1[s1 + mid];
        int k2 = s2 + mid >= n? Integer.MAX_VALUE: nums2[s2 + mid];
        if (k1 > k2) {
            return findKthElem(nums1, nums2, s1, s2 + Math.floorDiv(k, 2), k - Math.floorDiv(k, 2));
        } else {
            return findKthElem(nums1, nums2, s1 + Math.floorDiv(k, 2), s2, k - Math.floorDiv(k, 2));
        }
    }
}
