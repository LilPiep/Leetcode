public class Solution {
    public int MostWordsFound(string[] sentences) {
        int ans = 0;
        foreach(string s in sentences){
            int current = s.Count(c => c == ' ') + 1;
            ans = Math.Max(current, ans);
        }
        return ans;
    }
}