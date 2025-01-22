public class Solution {
    public int EqualPairs(int[][] grid) {
        int ans = 0;
        int n = grid[0].Length;

        Dictionary<string, int> rowDict = new Dictionary<string, int>();

        for (int i = 0; i < n; i++) {
            string row = string.Join(",", grid[i]);
            if (rowDict.ContainsKey(row)) {
                rowDict[row]++;
            } else {
                rowDict[row] = 1;
            }
        }

        for (int j = 0; j < n; j++) {
            List<int> column = new List<int>();
            for (int i = 0; i < n; i++) {
                column.Add(grid[i][j]);
            }
            string col = string.Join(",", column);

            if (rowDict.ContainsKey(col)) {
                ans += rowDict[col];
            }
        }
        return ans;
    }
}