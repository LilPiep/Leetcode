public class Solution {
    public int NumberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int ans = 0;
        foreach(int h in hours){
            if(h>=target)
                ans++;
        }
        return ans;
    }
}