# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def linkedListToInt(self, l):
        s = ""
        while l:
            s += str(l.val)
            l = l.next
        s = s[::-1]
        i = int(s)
        return i
        
    def addTwoNumbers(self, l1, l2):
        i1 = self.linkedListToInt(l1)
        i2 = self.linkedListToInt(l2)
        i3 = i1 + i2
        s3 = str(i3)[::-1]
        ans = ListNode(int(s3[0])) 
        current = ans
        for char in s3[1:]:
            current.next = ListNode(int(char))
            current = current.next
        return ans