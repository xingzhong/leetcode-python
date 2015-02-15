# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None : return None
        pilot = head.val
        curr = head.next
        prev = head
        while curr :
            if curr.val != pilot :
                pilot = curr.val
                prev = prev.next
            else:
                prev.next = curr.next
            curr = curr.next
        return head
