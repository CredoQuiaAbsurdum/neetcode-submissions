class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}

        def pathFromLocation(r, c):
            if r == m or c == n or obstacleGrid[r][c] == 1:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            if r == m - 1 and c == n - 1:
                memo[(r, c)] = 1
                return memo[(r, c)]
            else:
                memo[(r, c)] = pathFromLocation(r + 1, c) + pathFromLocation(r, c + 1)
                return memo[(r, c)]

        return pathFromLocation(0, 0)
            
        