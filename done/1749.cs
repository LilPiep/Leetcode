public class Solution {
    public int MaxAbsoluteSum(int[] nums) {
        int maxSum = 0, minSum = 0, maxEnding = 0, minEnding = 0;

        foreach (int num in nums) {
            maxEnding = Math.Max(maxEnding + num, num);
            maxSum = Math.Max(maxSum, maxEnding);

            minEnding = Math.Min(minEnding + num, num);
            minSum = Math.Min(minSum, minEnding);
        }

        return Math.Max(maxSum, Math.Abs(minSum));
    }
}