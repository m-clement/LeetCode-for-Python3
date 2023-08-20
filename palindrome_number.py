class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original_x, reversed_x = x, 0
        
        while x > 0:
            pop = x % 10
            x //= 10
            reversed_x = reversed_x * 10 + pop
        
        return original_x == reversed_x
