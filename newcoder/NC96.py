class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 
# @param head ListNode类 the head
# @return bool布尔型
#
class Solution:
    def isPail(self , head ):
        origin = ""
        reverse = ""

        # 反转链表
        pre = None
        cur = head
        while cur != None:
            origin += str(cur.val)
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        
        # 填充reverse链表
        cur = pre
        while cur != None:
            reverse += str(cur.val)
            cur = cur.next
        
        if origin == reverse:
            return True
        else:
            return False