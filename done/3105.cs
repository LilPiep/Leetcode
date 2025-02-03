public class Solution {
    public int LongestMonotonicSubarray(int[] nums) {
        if (nums.Length == 0) return 0; 
        int bestIncreasing = 1, bestDecreasing = 1;
        int currentIncreasing = 1, currentDecreasing = 1;
        for (int i = 0; i < nums.Length - 1; i++) {
            if (nums[i] < nums[i + 1]) {
                currentIncreasing++;
                bestIncreasing = Math.Max(bestIncreasing, currentIncreasing);
                currentDecreasing = 1;
            } 
            else if (nums[i] > nums[i + 1]) {
                currentDecreasing++;
                bestDecreasing = Math.Max(bestDecreasing, currentDecreasing);
                currentIncreasing = 1;
            } 
            else {
                currentIncreasing = 1;
                currentDecreasing = 1;
            }
        }
        return Math.Max(bestIncreasing, bestDecreasing);
    }
}