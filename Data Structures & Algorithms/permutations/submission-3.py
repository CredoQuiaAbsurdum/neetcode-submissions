class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def helper(i, permutation):
            if i >= len(nums):
                result.append(permutation.copy())
                return
            for j in range(len(permutation) + 1):
                permutation.insert(j, nums[i])
                helper(i + 1, permutation)
                permutation.pop(j)
        

        helper(0, [])
        return result


        