# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        prev = None
        nex = head.next
        while nex:
            curr.next = prev
            prev = curr
            curr = nex
            nex = nex.next
        curr.next = prev
        return curr