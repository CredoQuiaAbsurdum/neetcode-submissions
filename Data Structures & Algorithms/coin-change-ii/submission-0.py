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
            
            count = 0
            for j in range(i, len(coins)):
                count += helper(j, remain - coins[j])
            memo[(i, remain)] = count
            return count
        
        return helper(0, amount)

        