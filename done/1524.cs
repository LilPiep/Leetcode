public class Solution {
    public int NumOfSubarrays(int[] arr) {
        int oddCount = 0, evenCount = 1;
        int sum = 0, ans = 0;
        int MOD = 1_000_000_007;

        foreach (int num in arr) {
            sum += num;
            if (sum % 2 == 1) {
                ans = (ans + evenCount) % MOD;
                oddCount++;
            } else { 
                ans = (ans + oddCount) % MOD;
                evenCount++;
            }
        }

        return ans;
    }
}