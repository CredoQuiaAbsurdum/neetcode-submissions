class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = collections.defaultdict(int)
        memo[1], memo[2]= 1, 2
        def dfs(remain):
            if remain in memo:
                return memo[remain]
            else:
                memo[remain] = dfs(remain - 1) + dfs(remain - 2)
                return memo[remain]

        return dfs(n)
        