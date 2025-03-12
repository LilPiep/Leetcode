public class Solution {
    public IList<IList<int>> FindMatrix(int[] nums) {
        List<int> numList = new List<int>(nums);
        List<List<int>> ans = new List<List<int>>();

        while(numList.Count != 0) { 
            List<int> temp = new List<int>();
            foreach(int n in numList.ToArray()) { 
                if(!temp.Contains(n)) {
                    temp.Add(n);
                }
            }
            ans.Add(temp);
            foreach(int n in temp) {
                numList.Remove(n);
            }
        }
        return ans.Cast<IList<int>>().ToList(); 
    }
}
