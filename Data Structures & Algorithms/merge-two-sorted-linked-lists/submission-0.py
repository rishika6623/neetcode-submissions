# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1_ptr = list1
        l2_ptr = list2
        l3 = ListNode(0)
        l4 = l3
        while l1_ptr and l2_ptr:
            if l1_ptr.val < l2_ptr.val:
                l3.next = l1_ptr
                l1_ptr = l1_ptr.next
            else:
                l3.next = l2_ptr
                l2_ptr = l2_ptr.next
            l3 = l3.next
        if not l1_ptr:
            l3.next = l2_ptr
        else:
            l3.next = l1_ptr
        return l4.next

            