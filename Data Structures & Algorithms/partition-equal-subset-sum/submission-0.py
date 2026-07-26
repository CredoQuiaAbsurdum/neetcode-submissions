class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 == 1:
             return False
        
        target = total / 2

        def helper(i, remain):
            if remain == 0:
                return True
            if remain < 0 or i >= len(nums):
                return False
            return helper(i + 1, remain - nums[i]) or helper(i + 1, remain)
        
        return helper(0, target)
        