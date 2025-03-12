public class Solution {
    public int SubtractProductAndSum(int n) {
        int s = 0;
        int p = 1;
        while (n > 0) {
            int digit = n % 10;
            s += digit;
            p *= digit; 
            n /= 10; 
        }
        return p - s;
    }
}
