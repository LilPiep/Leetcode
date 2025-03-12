public class Solution {
    public int BalancedStringSplit(string s) {
        Dictionary<char, int> d = new Dictionary<char, int> {
            {'L', 0},
            {'R', 0}
        };
        int ans = 0;
        foreach(char c in s){
            d[c] += 1;
            if(d['L'] == d['R'] && d['L'] != 0){
                ans += 1;
                d['L'] = 0;
                d['R'] = 0;
            }
        }
        return ans;
    }
}