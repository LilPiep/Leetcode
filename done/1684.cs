public class Solution {
    public int CountConsistentStrings(string allowed, string[] words) {
        int ans = 0;
        foreach(string w in words){
            int temp = w.Length;
            foreach(char c in w){
                if(allowed.Contains(c)){
                    temp --;
                }
            }
            if (temp == 0){
                ans ++;
            }
        }
        return ans;
    }
}