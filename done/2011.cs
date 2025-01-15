public class Solution {
    public int FinalValueAfterOperations(string[] operations) {
        int ans = 0;
        foreach(string s in operations){
            if (s.Contains("-")){
                ans--;
            }
            else{
                ans++;
            }
        }
        return ans;
    }
}