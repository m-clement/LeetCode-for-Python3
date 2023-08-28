class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: if both are None, they are the same
        if not p and not q:
            return True
        
        # If one of them is None and the other isn't, they are not the same
        if not p or not q:
            return False
        
        # If the values of nodes p and q are different, they are not the same
        if p.val != q.val:
            return False
        
        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)