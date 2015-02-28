# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None : return None
        curr = head
        dummy = ListNode(-1)
        dummy.next = head
        curr, prev = head, dummy
        while curr and curr.next :
            prev.next = curr.next
            nn = curr.next.next
            curr.next.next = curr
            curr.next = nn
            curr, prev = curr.next, curr

        return dummy.next
