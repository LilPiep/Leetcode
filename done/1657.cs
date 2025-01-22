public class Solution {
    public bool CloseStrings(string word1, string word2) {
        if (word1.Length != word2.Length){
            return false;
        }

        Dictionary<char, int> recap1 = new Dictionary<char, int>();
        Dictionary<char, int> recap2 = new Dictionary<char, int>();

        foreach (char c in word1){
            if (recap1.ContainsKey(c)){
                recap1[c] += 1;
            }
            else{
                recap1[c] = 1;
            }
        }

        foreach (char c in word2){
            if (recap2.ContainsKey(c)){
                recap2[c] += 1;
            }
            else{
                recap2[c] = 1;
            }
        }

        if (!recap1.Keys.OrderBy(c => c).SequenceEqual(recap2.Keys.OrderBy(c => c))) {
            return false;
        }

        if (!recap1.Values.OrderBy(f => f).SequenceEqual(recap2.Values.OrderBy(f => f))) {
            return false;
        }

        return true;
    }
}