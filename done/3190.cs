public class Solution {
    public int MinimumOperations(int[] nums) {
        int ans = 0;
        foreach (int n in nums){
            if(n%3 != 0){
                ans++;
            }
        }
        return ans;
    }
}