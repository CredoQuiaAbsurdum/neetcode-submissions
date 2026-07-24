class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def helper(i, current):
            nonlocal result

            if i == len(nums):
                result.append(current.copy())
            else:
                current.append(nums[i])
                helper(i + 1, current)
                current.pop()
                helper(i + 1, current)
        
        helper(0, [])
        return result

