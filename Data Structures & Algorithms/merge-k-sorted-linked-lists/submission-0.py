# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy_copy = dummy
        all_ptrs = []

        for i, elem in enumerate(lists):
            if elem:
                heapq.heappush(all_ptrs, (elem.val, i))

        while all_ptrs:
            elem, index = heapq.heappop(all_ptrs)
            dummy.next = lists[index]
            dummy = dummy.next 
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(all_ptrs, (lists[index].val, index))

        return dummy_copy.next



        