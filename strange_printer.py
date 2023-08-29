class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}
        
        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Initialize the result with maximum possible turns
            ans = dp(i + 1, j) + 1
            
            # Iterate over possible splitting points
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    ans = min(ans, dp(i, k - 1) + dp(k + 1, j))
            
            memo[(i, j)] = ans
            return ans
        
        return dp(0, len(s) - 1)


