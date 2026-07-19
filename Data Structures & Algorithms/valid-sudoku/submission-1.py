class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
        cols = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
        box = [[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]

        for i in range(9):
            for j in range(9):
                # print(rows, cols, box)
                # print()
                check = board[i][j]
                if check != ".":
                    # row
                    if check in rows[i]:
                        return False
                    rows[i].add(check)
                    # col
                    if check in cols[j]:
                        return False
                    cols[j].add(check)
                    # box
                    if check in box[i//3][j//3]:
                        return False
                    box[i//3][j//3].add(check)
        return True