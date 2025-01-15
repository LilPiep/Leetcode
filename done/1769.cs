using System;
using System.Collections.Generic;

public class Solution {
    public int[] MinOperations(string boxes) {
        int n = boxes.Length;
        int[] ans = new int[n];

        for (int i = 0; i < n; i++) {
            int temp = 0;
            for (int j = 0; j < n; j++) {
                if (boxes[j] == '1') {
                    temp += Math.Abs(j - i);
                }
            }
            ans[i] = temp;
        }
        return ans;
    }
}