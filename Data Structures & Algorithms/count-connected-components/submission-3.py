class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        if n == 0 or n == 1:
            return n
        
        neighbors = {}
        for a, b in edges:
            if a not in neighbors:
                neighbors[a] = set()
            neighbors[a].add(b)
            if b not in neighbors:
                neighbors[b] = set()
            neighbors[b].add(a)
        
        # n - len(neighbors)
        visited = set()
        def dfs(i):
            visited.add(i)
            for neighbor in neighbors.get(i, set()):
                if neighbor not in visited:
                    dfs(neighbor)
        
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count

        