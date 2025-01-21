import java.io.*;

class Solution {
    public String convertDateToBinary(String date) {
        String[] sub = date.split("-");
        String ans = "";
        for (String s : sub) {
            int i = Integer.parseInt(s);
            ans += Integer.toBinaryString(i);
            ans += "-";
        }
        return ans.substring(0, ans.length() - 1);
    }
}