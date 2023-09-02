class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase
        s = s.lower()
        
        # Initialize two pointers
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move the left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            
            # Move the right pointer to the previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare the characters at the two pointers
            if s[left] != s[right]:
                return False
            
            # Move the pointers towards each other
            left += 1
            right -= 1
        
        return True
