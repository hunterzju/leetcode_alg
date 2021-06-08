# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next != None and cur.next.next != None:
            tmp = cur.next
            tmp_next = cur.next.next.next
            
            cur.next = cur.next.next
            cur.next.next = tmp
            cur.next.next.next = tmp_next

            cur = cur.next.next

        return dummy.next
