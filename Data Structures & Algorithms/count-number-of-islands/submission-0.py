class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        check_next = []
        islands = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        #find first
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b] == "1" and (a, b) not in visited:
                    check_next.append((a, b))
                    islands += 1
                    visited.add((a, b))    

                while check_next:
                    i, j = check_next.pop()
                    for x, y in directions:
                        if i + x >= 0 and i + x < len(grid) and j + y >= 0 and j + y < len(grid[0]) and (i+x, j+y) not in visited and grid[i+x][j+y] == "1":
                            check_next.append((i+x, j+y))
                            visited.add((i+x, j+y))
        
        return islands