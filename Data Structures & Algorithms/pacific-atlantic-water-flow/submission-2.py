class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        n, m = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        atlantic, pacific = set(), set()

        def dfs(r, c, visited):

            if (r, c) in visited:
                return
            
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                
                if heights[nr][nc] >=heights[r][c]:
                    dfs(nr, nc, visited)
            
        for r in range(n):
            dfs(r, 0, pacific)
        for c in range(m):
            dfs(0, c, pacific)

        for r in range(n):
            dfs(r, m - 1, atlantic)
        for c in range(m):
            dfs(n - 1, c, atlantic)

        result = []
        for r in range(n):
            for c in range(m):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append((r, c))
        
        return result
        










