public class Solution {
    public int[] RunningSum(int[] nums) {
        int n = nums.Length;
        int[] ans = new int[n];
        int current = 0;
        for(int i = 0; i < n; i++){
            current += nums[i];
            ans[i] = current; 
        }
        return ans;
    }
}