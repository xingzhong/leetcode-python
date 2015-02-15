# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head is None : return None
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        while curr and n > 0:
            curr = curr.next
            n -= 1
        if n > 0 : 
            return head
        slow = dummy
        while curr.next:
            slow = slow.next
            curr = curr.next
        if slow.next:
            slow.next = slow.next.next
        else:
            slow.next = None
        return dummy.next
        
