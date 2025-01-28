public class Solution {
    public int FindMaxFish(int[][] grid) {
        int rows = grid.Length;
        int cols = grid[0].Length;
        int best = 0;

        int DFS(int[][] grid, int i, int j) {
            if (i < 0 || i >= rows || j < 0 || j >= cols || grid[i][j] == 0)
                return 0;

            int fish = grid[i][j];
            grid[i][j] = 0;

            fish += DFS(grid, i + 1, j); // Bas
            fish += DFS(grid, i - 1, j); // Haut
            fish += DFS(grid, i, j + 1); // Droite
            fish += DFS(grid, i, j - 1); // Gauche

            return fish;
        }

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] != 0) {
                    // Effectuer un DFS à partir de cette cellule
                    best = Math.Max(best, DFS(grid, i, j));
                }
            }
        }

        return best;
    }
}