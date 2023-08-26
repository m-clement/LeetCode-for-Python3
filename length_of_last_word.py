class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing spaces
        s = s.rstrip()
        
        # Split string into words
        words = s.split(' ')

        # Return length of last word
        return len(words[-1])






