class Solution:
    def mySqrt(self, x: int) -> int:
        # Initialize left and right pointers
        left = 0
        right = x
        
        while left <= right:
            # Set mid to the average of left and right
            mid = (left + right) // 2
            
            # If mid * mid is less than or equal to x
            if mid * mid <= x:
                # Set left to mid + 1
                left = mid + 1
            # If mid * mid is greater than x
            else:
                # Set right to mid - 1
                right = mid - 1
        
        # Return right
        return right