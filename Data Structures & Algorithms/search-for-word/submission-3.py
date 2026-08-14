class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visit = set()

        def dfs(i, j, index):
            if index == len(word):
                return True

            if (
                i < 0 or i >= rows or
                j < 0 or j >= cols or
                (i, j) in visit or
                board[i][j] != word[index]
            ):
                return False

            visit.add((i, j))

            for di, dj in directions:
                if dfs(i + di, j + dj, index + 1):
                    return True

            # Backtrack
            visit.remove((i, j))

            return False

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False