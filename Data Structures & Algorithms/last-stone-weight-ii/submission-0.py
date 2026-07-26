class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        total = sum(stones)
        target = total // 2

        memo = {}

        def helper(i, current):

            if current > target:
                return -1

            if i == len(stones):
                return current

            if (i, current) in memo:
                return memo[(i, current)]

            pick = helper(i + 1, current + stones[i])
            skip = helper(i + 1, current)

            memo[(i, current)] = max(pick, skip)

            return memo[(i, current)]

        half = helper(0, 0)

        return total - 2 * half