# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val: int):
        tmp_head = ListNode(0, head)
        tmp_node = tmp_head.next
        pre_node = tmp_head
        while tmp_node != None:
            if tmp_node.val == val:
                pre_node.next = tmp_node.next
                tmp_node = tmp_node.next
            else:
                pre_node = tmp_node
                tmp_node = tmp_node.next
        return tmp_head.next

if __name__ == "__main__":
    sol = Solution()
    
            
