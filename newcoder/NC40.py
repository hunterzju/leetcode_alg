class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
# 
# @param head1 ListNode类 
# @param head2 ListNode类 
# @return ListNode类
#
class Solution:
    def addInList(self , head1 , head2 ):
        cur1, cur2 = head1, head2
        pre1, pre2 = None, None
        cnt1, cnt2 = 0, 0
        
        # 将两个链表反转
        while cur1 != None:
            cnt1 += 1
            tmp = cur1.next 
            cur1.next = pre1
            pre1 = cur1
            cur1 = tmp
        
        while cur2 != None:
            cnt2 += 1
            tmp = cur2.next
            cur2.next = pre2 
            pre2 = cur2
            cur2 = tmp
        
        # 比较长度，并交换，pre1指向长链表，pre2指向短链表
        if cnt1 < cnt2:
            pre1, pre2 = pre2, pre1
        
        # 计算各节点和
        cur1, cur2 = pre1, pre2
        ci = 0
        ppre1 = pre1        # 防止cnt1 == cnt2
        while pre2 != None:
            pre_ci = ci
            ci = (pre1.val + pre2.val + pre_ci) // 10
            pre1.val = (pre1.val + pre2.val + pre_ci) % 10
            ppre1 = pre1
            pre1 = pre1.next 
            pre2 = pre2.next 

        while ci:
            if pre1 != None:
                pre_ci = ci
                ci = (pre1.val + pre_ci) // 10
                pre1.val = (pre1.val + pre_ci) % 10
                pre1 = pre1.next
            else:
                ci_node = ListNode(ci)
                ci_node.next = None
                ppre1.next = ci_node
    
        # 反转head1
        pre1 = None
        while cur1 != None:
            tmp = cur1.next 
            cur1.next = pre1
            pre1 = cur1
            cur1 = tmp
        return pre1

        
        

        

