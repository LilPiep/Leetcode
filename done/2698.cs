public class Solution {
    public int PunishmentNumber(int n) {
        int totalSum = 0;

        for (int i = 1; i <= n; i++) {
            int square = i * i;
            if (CanPartition(square.ToString(), i)) {
                totalSum += square;
            }
        }

        return totalSum;
    }

    private bool CanPartition(string numStr, int target) {
        int length = numStr.Length;

        // Backtracking function to check if we can partition
        bool Backtrack(int start, int currentSum) {
            if (currentSum > target) return false;
            if (start == length) return currentSum == target;

            for (int end = start + 1; end <= length; end++) {
                // Get the substring and convert to integer
                string partStr = numStr.Substring(start, end - start);
                int part = int.Parse(partStr);
                if (Backtrack(end, currentSum + part)) {
                    return true;
                }
            }
            return false;
        }

        return Backtrack(0, 0);
    }
}