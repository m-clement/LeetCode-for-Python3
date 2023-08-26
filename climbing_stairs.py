class Solution:
    def climbStairs(self, n: int) -> int:

        # Base cases
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        # Initialize an array ways of size n
        ways = [0] * n
        # Initialize the first two value based on the base cases
        ways[0] = 1
        ways[1] = 2

        for i in range(2, n):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[n - 1]
