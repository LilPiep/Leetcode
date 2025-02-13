public class Solution {
    public int FindKthLargest(int[] nums, int k) {
        PriorityQueue<int, int> pq = new PriorityQueue<int, int>();
        foreach(int val in nums){
            pq.Enqueue(val, val);
            if (pq.Count > k) {
                pq.Dequeue();
            }
        }
        return pq.Peek();
    }
}