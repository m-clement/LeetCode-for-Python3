class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_safe(board, row, col):
            # Check column
            for i in range(row):
                if board[i] == col or \
                   board[i] - i == col - row or \
                   board[i] + i == col + row:
                    return False
            return True

        def solve(board, row):
            nonlocal count
            if row == n:
                count += 1
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(board, row + 1)
                    board[row] = -1

        count = 0
        solve([-1]*n, 0)
        return count
