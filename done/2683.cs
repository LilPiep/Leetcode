public class Solution {
    public bool DoesValidArrayExist(int[] derived) {
        int ans = 0;
        foreach(int d in derived){
            ans ^= d;
        }
        if(ans==1){
            return false;
        }
        return true;
    }
}