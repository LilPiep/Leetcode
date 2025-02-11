public class Solution {
    public int MinFlips(int a, int b, int c) {
        int aorb =a|b;
        int ans = 0;
        for(int i=0;i<32;i++)
        {
            if((aorb>>i&1) != (c>>i&1))
            {
                if((c>>i&1)==0 && (a>>i &1)==1 && (b>>i&1)==1)
                    ans+=2;
                else
                    ans++;
            }
        }
        return ans;
    }
}