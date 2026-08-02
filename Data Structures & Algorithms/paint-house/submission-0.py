class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        memo = {}

        def helper(i, prev):
            if i >= len(costs):
                return 0
            if (i, prev) in memo:
                return memo[(i, prev)]
            
            result = float('inf')
            for color in range(3):
                cost = costs[i][color]
                if color != prev:
                    result = min(result, cost + helper(i + 1, color))
            memo[(i, prev)] = result
            return memo[(i, prev)]
        
        return helper(0, -1)

        

            