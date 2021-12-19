# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(next=head)
        preNode = dummy
        tarNode = dummy
        cur = dummy
        cnt = 0
        while cur != None:
            cur = cur.next
            cnt += 1
            if(cnt - n) >= 0:
                preNode = tarNode
                tarNode = tarNode.next
        preNode.next = tarNode.next
        return dummy.next
