public class Solution {
    public int SmallestEvenMultiple(int n) {
        int ans = 2;
        while(ans%n != 0){
            ans += 2;
        }
        return ans;
    }
}