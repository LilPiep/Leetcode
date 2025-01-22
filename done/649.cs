public class Solution {
    public string PredictPartyVictory(string senate) {
        int rCount = 0;
        int dCount = 0;
        Queue<char> q = new Queue<char>();

        for (int i = 0; i < senate.Length; i++)
        {
            q.Enqueue(senate[i]);
            if (senate[i] == 'R')
                rCount++;
            else
                dCount++;
        }

        int rBanCount = 0;
        int dBanCount = 0;
        while (rCount > 0 && dCount > 0)
        {
            char c = q.Dequeue();
            if (c == 'R')
            {
                if (rBanCount > 0)
                {
                    rBanCount--;
                    rCount--;
                }
                else
                {
                    dBanCount++;
                    q.Enqueue('R');
                }
            }
            else
            {
                if (dBanCount > 0)
                {
                    dBanCount--;
                    dCount--;
                }
                else
                {
                    rBanCount++;
                    q.Enqueue('D');
                }
            }
        }

        return ((rCount == 0) ? "Dire" : "Radiant");
    }
}