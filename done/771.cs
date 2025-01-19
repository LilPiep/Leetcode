using System;
using System.Linq;

public class Solution {
    public int NumJewelsInStones(string jewels, string stones) {
        int ans = 0;
        foreach (char c in jewels){
            ans += stones.Count(f => (f == c));
        }
        return ans;
    }
}