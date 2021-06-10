# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param pHead1 ListNode类 
# @param pHead2 ListNode类 
# @return ListNode类
#
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        len1, len2 = 0, 0
        cur1, cur2 = pHead1, pHead2
        while(cur1!= None):
            len1 += 1
            cur1 = cur1.next 
        while(cur2!=None):
            len2 += 1
            cur2 = cur2.next 

        if len1 >= len2:
            res = len1 - len2
            cur1 = pHead1
            cur2 = pHead2
            while(res > 0):
                cur1 = cur1.next 
                res -= 1
        else:
            res = len2 - len1 
            cur1 = pHead1
            cur2 = pHead2
            while(res > 0):
                cur2 = cur2.next 
                res -= 1
        
        while(cur1 != None):
            if(cur1 == cur2):
                return cur1
            cur1 = cur1.next 
            cur2 = cur2.next 
        return None