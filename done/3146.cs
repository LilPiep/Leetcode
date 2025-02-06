public class Solution {
    public int FindPermutationDifference(string s, string t) {
        int ans = 0;
        Dictionary<char, int> indexMap = new Dictionary<char, int>();
        for (int i = 0; i < t.Length; i++) {
            indexMap[t[i]] = i;
        }
        for (int i = 0; i < s.Length; i++) {
            ans += Math.Abs(i - indexMap[s[i]]);
        }
        return ans;
    }
}