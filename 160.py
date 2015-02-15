# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        ca, cb = headA, headB
        flagA, flagB = False, False
        while ca != cb :
            ca = ca.next
            cb = cb.next
            if ca is None :
                if not flagA :
                    ca, flag = headB, True
                else:
                    return None
            if cb is None :
                if not flagB:
                    cb, flagB = headA, True
                else:
                    return None
            
        return ca
        
