class Trie
{
    class Node
    {
        public bool IsWord = false;
        public Node[] Children = new Node[26];
    }

    private Node Root;
    private Node curr;
    private List<string> resultBuffer;

    public Trie()
    {
        Root = new Node();
    }

    private void DfsWithPrefix(Node curr, string word)
    {
        if (resultBuffer.Count == 3)
            return;
        if (curr.IsWord)
            resultBuffer.Add(word);

        for (char c = 'a'; c <= 'z'; c++)
        {
            if (curr.Children[c - 'a'] != null)
                DfsWithPrefix(curr.Children[c - 'a'], word + c);
        }
    }

    public void Insert(string s)
    {
        curr = Root;
        foreach (char c in s)
        {
            if (curr.Children[c - 'a'] == null)
                curr.Children[c - 'a'] = new Node();
            curr = curr.Children[c - 'a'];
        }
        curr.IsWord = true;
    }

    public List<string> GetWordsStartingWith(string prefix)
    {
        curr = Root;
        resultBuffer = new List<string>();
        
        foreach (char c in prefix)
        {
            if (curr.Children[c - 'a'] == null)
                return resultBuffer;
            curr = curr.Children[c - 'a'];
        }
        
        DfsWithPrefix(curr, prefix);
        return resultBuffer;
    }
}

class Solution
{
    public IList<IList<string>> SuggestedProducts(string[] products, string searchWord)
    {
        Trie trie = new Trie();
        List<List<string>> result = new List<List<string>>();

        foreach (string w in products)
            trie.Insert(w);

        string prefix = "";
        foreach (char c in searchWord)
        {
            prefix += c;
            result.Add(trie.GetWordsStartingWith(prefix));
        }

        return result.ConvertAll(x => (IList<string>)x);
    }
}