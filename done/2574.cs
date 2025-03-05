public class Solution {
    public int[] LeftRightDifference(int[] nums) {
        List<int> ans = new List<int>();
        int left = 0;
        int right = 0;

        for(int i = 0; i < nums.Length; i++){
            right += nums[i];
        }
        
        for(int i = 0; i < nums.Length; i++){
            right -= nums[i];
            ans.Add(Math.Abs(left-right));
            left += nums[i];
        }
        return ans.ToArray();;
    }
}