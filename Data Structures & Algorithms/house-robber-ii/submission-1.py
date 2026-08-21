class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def maxRob(subarray):
            if not subarray:
                return 0
            memo = {}
            def solve(i):
                if i in memo:
                    return memo[i]
                if i == 0:
                    memo[i] = subarray[0]
                elif i == 1:
                    memo[i] = max(subarray[0], subarray[1])
                else:
                    memo[i] = max(subarray[i] + solve(i - 2), solve(i - 1))
                return memo[i]
            return solve(len(subarray) - 1)

        return max(maxRob(nums[1:]), maxRob(nums[:-1]))