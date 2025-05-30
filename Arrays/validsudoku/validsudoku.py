class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(row):
            currentValid = set()
            for string in row:
                if string != ".":
                    if string in currentValid:
                        return False
                    currentValid.add(string)
            return True

        for i in range(9):
            if not check(board[i]):
                return False
   
        transposed = zip(*board)
        for row in transposed:
            if not check(row):
                return False
        
        dividedGrid = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                subgrid = []
                for k in range(3):
                    for l in range(3):
                        subgrid.append(board[i + k][j + l])
                dividedGrid.append(subgrid)
        
        for row in dividedGrid:
            if not check(row):
                return False
        
        return True


        