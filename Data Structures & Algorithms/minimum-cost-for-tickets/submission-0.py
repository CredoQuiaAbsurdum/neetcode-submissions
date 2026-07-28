class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        memo = {}

        def helper(i):
            if i >= len(days):
                return 0
            if i in memo:
                return memo[i]

            res = float('inf')
            for j, duration in enumerate([1, 7, 30]):
                # Find the next index after the pass expires
                next_i = i
                while next_i < len(days) and days[next_i] < days[i] + duration:
                    next_i += 1
                
                res = min(res, costs[j] + helper(next_i))
            
            memo[i] = res
            return res

        return helper(0)