class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def helper(node):
            if not node:
                return 0
            
            # Recursively find the max path sum for left and right child
            left_max = max(helper(node.left), 0)
            right_max = max(helper(node.right), 0)
            
            # Update the global maximum
            self.max_sum = max(self.max_sum, left_max + right_max + node.val)
            
            # Return the max path sum that includes the current node
            return node.val + max(left_max, right_max)
        
        helper(root)
        return self.max_sum
