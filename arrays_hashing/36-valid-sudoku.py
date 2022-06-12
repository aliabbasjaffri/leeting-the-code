"""
checking a sudoku for valid configuration
leetcode url: https://leetcode.com/problems/valid-sudoku/
runtime complexity: 0(n^2)
space complexity: 0(n)
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def _check_valid_row(row: List[str]) -> bool:
            elements = set()
            for item in row:
                if not item == "." and item not in elements:
                    elements.add(item)
                elif not item == "." and item in elements:
                    return False
            return True
        
        def _check_valid_column(board: List[List[str]], column: int) -> bool:
            elements = set()
            for row in range(9):
                if not board[row][column] == "." and board[row][column] not in elements:
                    elements.add(board[row][column])
                elif not board[row][column] == "." and board[row][column] in elements:
                    return False
            return True
        
        def _valid_box_rows(board: List[List[str]], row: int, column: int) -> bool:
            for i in range(3):
                elements = set()
                for item in board[row+i]:
                    if not item == "." and item not in elements:
                        elements.add(item)
                    elif not item == "." and item in elements:
                        return False
                return True
        
        def _valid_box_columns(board: List[List[str]], row: int, column: int) -> bool:
            for col in range(column, column + 3):
                elements = set()
                for r in range(row, row + 3):
                    if not board[r][col] == "." and board[r][col] not in elements:
                        elements.add(board[r][col])
                    elif not board[r][col] == "." and board[r][col] in elements:
                        return False
                return True
        
        def check_valid_rows(board: List[List[str]]) -> bool:
            for i in range(9):
                if not _check_valid_row(board[i]):
                    return False
            return True
        
        def check_valid_columns(board: List[List[str]]) -> bool:
            for i in range(9):
                if not _check_valid_column(board, i):
                    return False
            return True
        
        def check_valid_sub_box(board: List[List[str]]) -> bool:
            starting_points = [0, 3, 6]
            for i in starting_points:
                for j in starting_points:
                    if not _valid_box_rows(board, i, j) or not _valid_box_columns(board, i, j):
                        return False
            return True
        
        return check_valid_rows(board) and check_valid_columns(board) and check_valid_sub_box(board)