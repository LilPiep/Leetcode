public class Solution {
    public bool IsArraySpecial(int[] nums) {
        for(int i = 1; i < nums.Length; i++){
            if((nums[i]+nums[i-1])%2==0){
                return false;
            }
        }
        return true;
    }
}