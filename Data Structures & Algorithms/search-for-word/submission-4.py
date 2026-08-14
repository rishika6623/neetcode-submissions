class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visit = set()

        def dfs(i, j, index):
            if index == len(word) - 1:
                return True

            visit.add((i, j))

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if (
                    0 <= ni < rows
                    and 0 <= nj < cols
                    and (ni, nj) not in visit
                    and board[ni][nj] == word[index + 1]
                ):
                    if dfs(ni, nj, index + 1):
                        return True

            visit.remove((i, j))
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False