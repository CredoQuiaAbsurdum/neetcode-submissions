class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        memo = {}
        def helper(i) -> List[int]:
            if i in memo:
                return memo[i]
    
            best_prev = []
            for j in range(i):
                if nums[j] < nums[i]:
                    candidate = helper(j)
                    if len(candidate) > len(best_prev):
                        best_prev = candidate
            
            memo[i] = best_prev + [nums[i]]
            return memo[i]

        maxLength = 0
        for i in range(len(nums)):
            maxLength = max(maxLength, len(helper(i)))

        return maxLength