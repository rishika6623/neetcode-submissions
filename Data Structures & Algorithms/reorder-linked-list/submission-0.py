# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        second_half = []

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        slow = slow.next

        while slow:
            second_half.append(slow)
            slow = slow.next

        print(second_half)

        top = head
        ptr = len(second_half) - 1

        while ptr >= 0:
            temp = top.next
            top.next = second_half[ptr]
            second_half[ptr].next = temp
            print(second_half[ptr])
            
            ptr -= 1
            top = temp
        
        top.next = None
