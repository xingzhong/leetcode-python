# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if not (l1 or l2): 
            return None
        head = ListNode(-1)
        curr = head
        over = False
        while l1 or l2:
            v1 = 0 if l1 is None else l1.val
            v2 = 0 if l2 is None else l2.val
            num = v1 + v2
            if over : num += 1
            over = False
            if num > 9 :
                over = True
                num -= 10
            curr.next = ListNode(num)
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            curr = curr.next
        if over: 
            curr.next = ListNode(1)
        return head.next
