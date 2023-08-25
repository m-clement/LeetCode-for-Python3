class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(num, row, col):
            # Check if the number is in the current row or column
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
            
            # Check if the number is in the current 3x3 box
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False
            return True
        
        def backtrack():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in map(str, range(1, 10)):
                            if is_valid(num, row, col):
                                board[row][col] = num
                                if backtrack():
                                    return True
                                board[row][col] = '.'
                        return False
            return True
        
        backtrack()
