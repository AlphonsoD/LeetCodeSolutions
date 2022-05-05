class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = dict()
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                else:
                    if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (squares.get((r//3,c//3)) != None and board[r][c] in squares[(r//3, c//3)]):
                        return False
                    else:
                        rows[r].add(board[r][c])
                        cols[c].add(board[r][c])
                        if squares.get((r//3, c//3)) == None:
                            squares[(r//3, c//3)] = set()
                        squares[(r//3, c//3)].add(board[r][c])
        
        return True