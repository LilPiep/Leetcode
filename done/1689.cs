public class Solution {
    public int MinPartitions(string n) {
        int max = 0;
        foreach(char c in n){
            int current = c - '0';
            if (current>max){
                max = current;
            }
        }
        return max;
    }
}