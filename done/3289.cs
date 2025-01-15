using System;
using System.Collections.Generic;

public class Solution {
    public int[] GetSneakyNumbers(int[] nums) {
        List<int> seen = new List<int>();
        List<int> ans = new List<int>();
        foreach(int n in nums){
            if (seen.Contains(n)){
                ans.Add(n);
            }
            else{
                seen.Add(n);
            }
        }
        return ans.ToArray();
    }
}