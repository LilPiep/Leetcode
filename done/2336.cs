public class SmallestInfiniteSet {

    private PriorityQueue<int, int> pq;
    private HashSet<int> inQueue; 

    public SmallestInfiniteSet() {
        pq = new PriorityQueue<int, int>();
        inQueue = new HashSet<int>();

        for (int i = 1; i < 1001; ++i) {
            pq.Enqueue(i, i);
            inQueue.Add(i);
        }
    }
    
    public int PopSmallest() {
        int smallest = pq.Dequeue();
        inQueue.Remove(smallest);
        return smallest;
    }
    
    public void AddBack(int num) {
        if (!inQueue.Contains(num)) {
            pq.Enqueue(num, num);
            inQueue.Add(num);
        }
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = new SmallestInfiniteSet();
 * int param_1 = obj.PopSmallest();
 * obj.AddBack(num);
 */