public class Solution {
    public int MaxWidthOfVerticalArea(int[][] points) {
        List<int> l = new List<int>();
        int ans = 0;
        int temp = 0;
        foreach(int[] point in points){
            l.Add(point[0]);
        }
        l.Sort();
        for(int i = 0; i < l.Count - 1; i++){
            temp = l[i+1] - l[i];
            ans = Math.Max(temp, ans);
        }
        return ans;
    }
}