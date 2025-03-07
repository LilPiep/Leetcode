public class Solution {
    public int[] FindMissingAndRepeatedValues(int[][] grid) {
        int len = grid.Length * grid[0].Length;
        Dictionary<int,int> d = new Dictionary<int,int>();

        for(int i = 1; i < len + 1; i++){
            d[i] = 0;
        }
        foreach(int[] tab in grid){
            foreach(int num in tab){
                d[num]++;
            }
        }

        int repeated = -1, missing = -1;
        foreach (var kvp in d) {
            if (kvp.Value == 2) {
                repeated = kvp.Key;
            }
            if (kvp.Value == 0) {
                missing = kvp.Key;
            }
        }

        return new int[] { repeated, missing };
    }
}