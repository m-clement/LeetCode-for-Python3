class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse a sublist of linked list
        def reverse_sublist(start, end):
            prev, curr = None, start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        # Helper function to count the number of nodes in the linked list
        def count_nodes(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        
        total_nodes = count_nodes(head)
        
        # Create a dummy node to act as the new head
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy  # end of the previous group
        
        while total_nodes >= k:
            group_start = prev_group_end.next
            group_end = prev_group_end.next
            
            # Move group_end to the end of the next group of k nodes
            for _ in range(k):
                group_end = group_end.next
            
            # Reverse the group of k nodes
            prev_group_end.next = reverse_sublist(group_start, group_end)
            
            # Move to the end of the reversed group
            group_start.next = group_end
            prev_group_end = group_start
            
            total_nodes -= k
        
        return dummy.next
