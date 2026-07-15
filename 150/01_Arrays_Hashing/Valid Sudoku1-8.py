'''
board =[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

board =[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
'''
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        for row in range(9):
            seen = set()
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
        for col in range(9):
            seen = set()
            for row in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
        for row in range(0,9,3):
            for col in range(0,9,3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        value = board[row+i][col+j]
                        if value == ".":
                            continue
                        if value in seen:
                            return False
                        seen.add(value)
        return True
#print(Solution().isValidSudoku(board))

        