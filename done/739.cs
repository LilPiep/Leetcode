public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        int n = temperatures.Length;
        int[] ans = new int[n];
        Stack<int> s = new Stack<int>();

        for(int i = 0; i < n ; i++) {
            while (s.Count > 0 && temperatures[s.Peek()] < temperatures[i]) {
                int index = s.Pop();
                ans[index] = i - index;
            }
            s.Push(i);
        }
        return ans;
    }
}