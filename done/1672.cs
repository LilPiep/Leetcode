public class Solution {
    public int MaximumWealth(int[][] accounts) {
        int max = 0;
        foreach(int[] account in accounts){
            int current = 0;
            foreach(int money in account){
                current += money;
            }
            if (current > max){
                max = current;
            }
        }
        return max;
    }
}