# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            first_node = head
            second_node = head.next
            
            # Swapping nodes
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            # Updating pointers
            prev = first_node
            head = first_node.next
        
        return dummy.next