public class Solution {
    public int[] SuccessfulPairs(int[] spells, int[] potions, long success) {
        Array.Sort(potions);
        var ans = new int[spells.Length];
        var current = 0;

        for(int i = 0; i < spells.Length; i++){
                int l = 0, r = potions.Length - 1;
                int leftMostIdx = -1;
                while(l <= r){
                    int m = (l + r) / 2;
                    if (((long)spells[i]) * potions[m] >= success){
                        leftMostIdx = m;
                        r = m - 1;
                    }
                    else l = m + 1;
                }
                ans[i] = leftMostIdx == -1 ? 0 : potions.Length - leftMostIdx;
            }
        return ans;
    }
}