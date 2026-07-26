class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def helper(i, current):
            if i == len(nums):
                if current == target:
                    return 1
                else:
                    return 0
            
            count = 0

            count += helper(i + 1, current - nums[i])
            count += helper(i + 1, current + nums[i])

            memo[(i, current)] = count

            return count
        

        return helper(0, 0)
