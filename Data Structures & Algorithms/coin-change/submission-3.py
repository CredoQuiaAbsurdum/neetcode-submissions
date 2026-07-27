class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def helper(remain):
            if remain == 0:
                return 0
            if remain < 0:
                return -1
            if remain in memo:
                return memo[remain]
            
            least = float('inf')
            for coin in coins:
                current = helper(remain - coin)
                if current >= 0:
                    least = min(least, current + 1)
            memo[remain] = -1 if least == float('inf') else least
            return memo[remain]
        
        return helper(amount)
