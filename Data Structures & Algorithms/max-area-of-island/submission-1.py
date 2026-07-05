class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r, c))
            current_area = 1
            for dr, dc in DIRECTIONS:
                current_area += dfs(r + dr, c + dc)
            return current_area
        
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(area, dfs(r, c))
        return area