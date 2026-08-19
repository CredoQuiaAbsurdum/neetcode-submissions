class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        if n == 1:
            return True
        treeMap = {}

        for a, b in edges:
            if a not in treeMap:
                treeMap[a] = set()
            treeMap[a].add(b)
            if b not in treeMap:
                treeMap[b] = set()
            treeMap[b].add(a)
        
        def dfs(num, visited):
            visited.add(num)
            if num in treeMap:
                for neighbor in treeMap[num]:
                    if neighbor not in visited:
                        dfs(neighbor, visited)
        
        visited = set()
        dfs(0, visited)
        return len(visited) == n