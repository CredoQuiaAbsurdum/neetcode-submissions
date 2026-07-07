class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        result = 0

        def dfs(i, xorsum):
            nonlocal result
            if i == len(nums):
                result += xorsum
                return
            
            dfs(i + 1, xorsum)
            dfs(i + 1, xorsum ^ nums[i])
        
        dfs(0, 0)
        return result