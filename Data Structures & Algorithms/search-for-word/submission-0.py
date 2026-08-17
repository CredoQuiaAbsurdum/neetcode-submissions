class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        if not board:
            return False

        n, m = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        path = set()
        def helper(x, y, word, i):
            if not (0 <= x < n and 0 <= y < m) or (x, y) in path:
                return False
            if board[x][y] == word[i]:
                if i == len(word) - 1:
                    return True
                else:
                    path.add((x, y))
                    for d in directions:
                        nx, ny = x + d[0], y + d[1]
                        if helper(nx, ny, word, i + 1):
                            return True
                    path.remove((x, y))
                    return False
            return False
        
        for r in range(n):
            for c in range(m):
                if helper(r, c, word, 0):
                    return True
        return False