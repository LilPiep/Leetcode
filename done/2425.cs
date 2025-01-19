using System;

public class Solution {
    public int XorAllNums(int[] nums1, int[] nums2) {
        int n1 = nums1.Length;
        int n2 = nums2.Length;
        int result = 0;
        if (n2 % 2 != 0) {
            foreach (int num in nums1) {
                result ^= num;
            }
        }
        if (n1 % 2 != 0) {
            foreach (int num in nums2) {
                result ^= num;
            }
        }
        return result;
    }
}