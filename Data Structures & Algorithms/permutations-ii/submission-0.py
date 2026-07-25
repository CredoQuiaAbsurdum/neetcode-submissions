class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        result = set()

        def helper(i, permutation):
            if i == len(nums):
                result.add(tuple(permutation))
                return
            for j in range(len(permutation) + 1):
                permutation.insert(j, nums[i])
                helper(i + 1, permutation)
                permutation.pop(j)

        helper(0, [])

        return [list(p) for p in result]