class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            result[i] = left
            left *= nums[i]

        right = 1
        for i in reversed(range(len(nums))):
            result[i] *= right
            right *= nums[i]

        return result