public class Solution {
    public int[] FindArray(int[] pref) {
        int n = pref.Length;
        int[] ans = new int[n];
        ans[0] = pref[0]; 

        for (int i = 1; i < n; i++) {
            ans[i] = pref[i] ^ pref[i - 1];
        }

        return ans;
    }
}
