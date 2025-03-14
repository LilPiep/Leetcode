public class Solution {
    public int MinOperations(int[] nums, int k) {
        List<int> list = nums.ToList();
        int ans = 0;
        while(true){
            int m = list.Min();
            if(m >= k){
                return ans;
            }
            list.Remove(m);
            ans++;
        }
    }
}