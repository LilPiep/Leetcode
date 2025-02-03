/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public int PairSum(ListNode head) {
        int best = 0;
        ListNode newList = null;
        ListNode current = head;
        ListNode currHalf = head;

        while (currHalf != null && currHalf.next != null) {
            currHalf = currHalf.next.next;
            ListNode temp = current.next;
            current.next = newList;
            newList = current;
            current = temp;
        }

        while (current != null) {
            best = Math.Max(best, current.val + newList.val);
            current = current.next;
            newList = newList.next;
        }
        
        return best;
    }
}