public class Solution {
    public int OrangesRotting(int[][] grid) {

        int n = grid.Length;
        int m = grid[0].Length;
        Queue<(int,int)> queue = new Queue<(int,int)>();
        bool[,] visited = new bool [n,m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 2) {
                    queue.Enqueue((i, j));
                    visited[i, j] = true;
                }
            }
        }

        int count = -1;
        int[][] directions = new int[][] {
            new int[] { -1, 0 },
            new int[] { 1, 0 },
            new int[] { 0, -1 },
            new int[] { 0, 1 }
        };

        while (queue.Count > 0) {
            int size = queue.Count;
            count++;
            for (int i = 0; i < size; i++) {
                var (row, col) = queue.Dequeue();

                foreach (var dir in directions) {
                    int nx = row + dir[0];
                    int ny = col + dir[1];
                    if (nx >= 0 && nx < n && ny >= 0 && ny < m 
                        && !visited[nx, ny] && grid[nx][ny] == 1) {
                        visited[nx, ny] = true;
                        grid[nx][ny] = 2;
                        queue.Enqueue((nx, ny));
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) {
                    return -1;
                }
            }
        }

        return count == -1 ? 0 : count;
    }
}