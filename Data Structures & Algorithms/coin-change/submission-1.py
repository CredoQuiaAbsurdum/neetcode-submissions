class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort(reverse=True)

        memo = {}
        def helper(remain, count):
            if remain == 0:
                return count
            if remain < 0:
                return -1
            if (remain, count) in memo:
                return memo[(remain, count)]
            
            least = float('inf')
            for coin in coins:
                current = helper(remain - coin, count + 1)
                if current >= 0:
                    least = min(least, current)
            if least == float('inf'):
                least = -1
            memo[(remain, count)] = least
            return least
        
        return helper(amount, 0)
