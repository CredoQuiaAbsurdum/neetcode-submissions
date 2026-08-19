class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False   
        if n == 1:
            return True
        
        neighbors = {}
        for a, b in edges:
            if a not in neighbors:
                neighbors[a] = set()
            neighbors[a].add(b)
            if b not in neighbors:
                neighbors[b] = set()
            neighbors[b].add(a)
        
        visited = set()
        def dfs(i):
            visited.add(i)
            for neighbor in neighbors.get(i, set()):
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(0)
        return len(visited) == n

        

        
        