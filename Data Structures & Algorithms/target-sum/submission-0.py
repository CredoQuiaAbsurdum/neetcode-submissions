class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        count = 0

        def helper(i, current):
            nonlocal count
            if i == len(nums):
                if current == target:
                    count += 1
                return
            
            helper(i + 1, current - nums[i])
            helper(i + 1, current + nums[i])
        
        helper(0, 0)
        return count
