class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        result = max(nums)
        maxP, minP = 1, 1
        for n in nums:
            if n == 0:
                maxP, minP = 1, 1
                continue

            tempMax = maxP
            maxP = max(n * maxP, n * minP, n)
            minP = min(n * tempMax, n * minP, n)
            result = max(result, maxP)
        
        return result