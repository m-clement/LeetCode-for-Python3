class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize the result list and stack
        res = []
        stack = []
        
        # Start with the root node
        current = root
        
        # Continue until the stack is empty or the current node is None
        while current or stack:
            # Push all the left nodes onto the stack
            while current:
                stack.append(current)
                current = current.left
            
            # Pop the top node from the stack
            current = stack.pop()
            # Add its value to the result list
            res.append(current.val)
            
            # Move to the right child
            current = current.right
        
        return res
