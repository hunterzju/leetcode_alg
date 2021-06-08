# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        curA = headA 
        curB = headB

        lenA = 0
        while curA != None:
            lenA += 1
            curA = curA.next
        
        lenB = 0
        while curB != None:
            lenB += 1
            curB = curB.next

        curA = headA
        curB = headB
        if lenA >= lenB:
            cnt = lenA - lenB
            while cnt > 0:
                curA = curA.next 
                cnt -= 1
        else:
            cnt = lenB - lenA
            while cnt > 0:
                curB = curB.next 
                cnt -= 1

        while curA != None and curB != None:
            if curA == curB:
                return curA
            curA = curA.next 
            curB = curB.next 

        return None
            
