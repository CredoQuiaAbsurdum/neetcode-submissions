class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = {}
        def helper(i, remain):
            if i >= len(coins) or remain < 0:
                return 0
            if remain == 0:
                return 1
            if (i, remain) in memo:
                return memo[(i, remain)]
            
            use = helper(i, remain - coins[i])
            skip = helper(i + 1, remain)

            memo[(i, remain)] = use + skip
            return memo[(i, remain)]
        
        return helper(0, amount)

        