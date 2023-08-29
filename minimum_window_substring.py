class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        
        # Create a frequency counter for characters in t
        t_freq = Counter(t)
        
        # Variables to keep track of the window
        left, right = 0, 0
        required_chars = len(t_freq)
        current_chars = 0
        window_counts = Counter()
        
        # Variables to keep track of the minimum window
        min_window_len = float('inf')
        min_window_start = 0
        
        while right < len(s):
            # Add character at right pointer to window_counts
            char = s[right]
            window_counts[char] += 1
            
            # If this character's count matches the required count in t, increase current_chars
            if char in t_freq and window_counts[char] == t_freq[char]:
                current_chars += 1
            
            # Contract the window from the left
            while left <= right and current_chars == required_chars:
                char = s[left]
                
                # Update the minimum window variables if needed
                if right - left + 1 < min_window_len:
                    min_window_len = right - left + 1
                    min_window_start = left
                
                # Move left pointer to the right
                window_counts[char] -= 1
                if char in t_freq and window_counts[char] < t_freq[char]:
                    current_chars -= 1
                
                left += 1
            
            # Expand the window from the right
            right += 1
        
        # If we found a valid window, return it
        return s[min_window_start:min_window_start + min_window_len] if min_window_len != float('inf') else ""

# Test the function
sol = Solution()
test_s = "ADOBECODEBANC"
test_t = "ABC"
sol.minWindow(test_s, test_t)
