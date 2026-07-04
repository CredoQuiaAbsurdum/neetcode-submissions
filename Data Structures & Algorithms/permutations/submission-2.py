class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []

        result = []
        
        def dfs(i, curr):

            if len(curr) == len(nums):
                result.append(curr.copy())
                return
            if i >= len(nums):
                return

            for j in range(len(curr) + 1):
                dfs(i + 1, curr[:j] + [nums[i]] + curr[j:])
        
        dfs(0, [])
        return result
