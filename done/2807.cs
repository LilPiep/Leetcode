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

    static int GCD(int a, int b)
    {
        return b == 0 ? a : GCD(b, a % b);
    }

    public ListNode InsertGreatestCommonDivisors(ListNode head) {
        ListNode current = head;
         while (current != null && current.next != null) {
            int gcdValue = GCD(current.val, current.next.val);
            ListNode gcdNode = new ListNode(gcdValue);
            gcdNode.next = current.next;
            current.next = gcdNode;
            current = gcdNode.next;
        }
        return head;
    }
}