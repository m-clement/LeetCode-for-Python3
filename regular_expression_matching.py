class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j] will be 'true' if the first i characters in s match the first j characters in p
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # the empty pattern can match the empty string
        dp[0][0] = True

        # Populate the rest of the column
        for j in range(1, n + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        # examine each character in s (i from 1 to m)
        # and each character in p (j from 1 to n)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] if s[i-1] == p[j-2] or p[j-2] == '.' else False)

        return dp[m][n]
