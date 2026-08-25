class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_reach = 0
        curr = 0

        while curr <= max_reach:
            max_reach = max(max_reach, curr + nums[curr])
            if max_reach >= len(nums) - 1:
                return True
            curr += 1

        return max_reach >= len(nums) - 1