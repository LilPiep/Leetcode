public class Solution {
    public IList<int> EventualSafeNodes(int[][] graph) {
        int n = graph.Length; 
        List<int> terminal = new List<int>();
        List<int> safe = new List<int>();
        bool[] isSafe = new bool[n];

        for (int i = 0; i < n; i++) {
            if (graph[i].Length == 0) {
                terminal.Add(i);
                isSafe[i] = true;
            }
        }

        bool updated;
        do {
            updated = false;
            for (int i = 0; i < n; i++) {
                if (!isSafe[i] && IsSafeNode(i, graph, isSafe)) {
                    isSafe[i] = true;
                    updated = true;
                }
            }
        } while (updated);

        for (int i = 0; i < n; i++) {
            if (isSafe[i]) {
                safe.Add(i);
            }
        }

        safe.Sort();
        return safe;
    }

    private bool IsSafeNode(int node, int[][] graph, bool[] isSafe) {
        foreach (int neighbor in graph[node]) {
            if (!isSafe[neighbor]) {
                return false;
            }
        }
        return true;
    }
}
