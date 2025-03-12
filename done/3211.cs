public class Solution {
    public IList<string> ValidStrings(int n) {
        List<string> ans = new List<string>();
        ProcessBackTrackingOnBList(ans, n, "0", 0);
        ProcessBackTrackingOnBList(ans, n, "1", 1);
        return ans;    
    }

    private void ProcessBackTrackingOnBList(List<string> ans, int n, string str, int bi)
    {
        if(str.Length == n)
        {          
            ans.Add(str);                
            return;
        }

        if(bi == 0)
        {
            ProcessBackTrackingOnBList(ans, n, str + 1, 1);
        }
        else
        { 
            ProcessBackTrackingOnBList(ans, n, str + 0, 0);
            ProcessBackTrackingOnBList(ans, n, str + 1, 1);
        }
    }
}