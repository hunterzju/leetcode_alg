class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 
# @param l1 ListNode类 
# @param l2 ListNode类 
# @return ListNode类
#
class Solution:
    def mergeTwoLists(self , l1 , l2 ):
        dummy_head = ListNode(0)
        cur = dummy_head
        while(l1 != None and l2 != None):
            if(l1.val >= l2.val):
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next 
            cur = cur.next
        if(l1 != None):
            cur.next = l1
        if(l2 != None):
            cur.next = l2
        return dummy_head.next
