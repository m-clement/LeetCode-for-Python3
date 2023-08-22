# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for idx, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, idx))
                lists[idx] = head.next
        
        dummy = ListNode()
        current = dummy
        
        while heap:
            val, idx = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next
            
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        
        return dummy.next