public class Solution {
    public int[] SmallerNumbersThanCurrent(int[] nums) {
        int current = 0;
        List<int> ans = new List<int>();
        for(int i = 0; i < nums.Length; i++){
            for(int j = 0; j < nums.Length; j++){
                if(nums[j] < nums[i]){
                    current++;
                }
            }
            ans.Add(current);
            current = 0;
        }
        return ans.ToArray();
    }
}