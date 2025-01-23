public class Solution {
    public int CountServers(int[][] grid) {
        int rows = grid.Length;
        int cols = grid[0].Length;
        
        Dictionary<int, int> lines = new Dictionary<int, int>();
        Dictionary<int, int> columns = new Dictionary<int, int>();

        for (int i = 0; i < rows; i++) {
            int countLines = 0; // 
            for (int j = 0; j < cols; j++) {
                countLines += grid[i][j];
                if (!columns.ContainsKey(j)) {
                    columns[j] = 0; 
                }
                columns[j] += grid[i][j]; 
            }
            lines[i] = countLines;
        }
        int totalServers = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1 && (lines[i] > 1 || columns[j] > 1)) {
                    totalServers++;
                }
            }
        }

        return totalServers;
    }
}