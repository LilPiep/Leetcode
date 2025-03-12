public class Solution {
    public int[] Decode(int[] encoded, int first) {
        int len = encoded.Length;
        int[] res = new int[len+1];
        res[0] = first;
        for(int i = 1; i < res.Length; i++)
        {
            res[i] = (res[i-1]^encoded[i-1]);
        }
        return res;
    }
}