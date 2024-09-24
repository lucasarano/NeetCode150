class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def checkCol(col):
            visit = set()
            for i in range(9):
                if board[i][col] != ".":
                    if board[i][col] in visit:
                        return False
                    visit.add(board[i][col])
            return True

        def checkRow(row):
            visit = set()
            for i in range(9):
                if board[row][i] != ".":
                    if board[row][i] in visit:
                        return False
                    visit.add(board[row][i])
            return True

        def checkQuad(row, col):
            visit = set()
            startRow, startCol = 3 * (row // 3), 3 * (col // 3)  # Calculate top-left corner of the 3x3 grid
            for i in range(3):
                for j in range(3):
                    num = board[startRow + i][startCol + j]
                    if num != ".":
                        if num in visit:
                            return False
                        visit.add(num)
            return True

        # Check all rows, columns, and 3x3 sub-grids
        for i in range(9):
            if not checkRow(i) or not checkCol(i):
                return False

        # Check 3x3 sub-grids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not checkQuad(i, j):
                    return False

        return True
