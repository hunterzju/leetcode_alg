class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @return ListNode类
#
class Solution:
    def oddEvenList(self , head ):
        dummy_even = ListNode(0)
        dummy_odd = ListNode(0)
        dummy_even.next, dummy_odd.next = None, None
        cur_even, cur_odd = dummy_even, dummy_odd
        
        cur = head
        idx = 1
        while cur != None:
            tmp = cur.next
            if idx % 2 == 0:
                cur_odd.next = cur
                cur_odd = cur_odd.next
                cur_odd.next = None
            else:
                cur_even.next = cur
                cur_even = cur_even.next
                cur_even.next = None
            cur = tmp
            idx += 1
        cur_even.next = dummy_odd.next
        return dummy_even.next
