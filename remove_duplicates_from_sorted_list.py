class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the current pointer
        current = head

        # Traverse the linked list
        while current and current.next:
            # If the current node's value is the same as the next node's value
            if current.val == current.next.val:
                # Skip the next node
                current.next = current.next.next
            else:
                # Move the current pointer forward
                current = current.next

        return head