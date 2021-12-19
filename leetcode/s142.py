# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        fast, slow = head, head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                p = head
                q = slow
                while p != q:
                    p = p.next 
                    q = q.next 
                return p 
        return None

