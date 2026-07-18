class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = {}
        def pathFromLocation(r, c):
            if r == m or c == n:
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
            
            
            
        