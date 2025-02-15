public class Solution {
    public int MinReorder(int n, int[][] connections) {
        List<List<(int sign, int conn)>> adj = new();
        int count = 0;

        for(int i = 0; i < n; i++){
            adj.Add(new List<(int sign, int conn)>()); 
        }

        foreach(int[] road in connections){
            adj[road[0]].Add((1, road[1]));
            adj[road[1]].Add((0, road[0])); 
        }

        DFS(0, -1);

        return count;

        void DFS(int curr, int par){            
            foreach((int sign, int conn) nei in adj[curr]){
                if(nei.conn == par) continue;
                count += nei.sign;
                DFS(nei.conn, curr);
            }
        }
    }
}