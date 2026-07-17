class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = collections.defaultdict(int)
        def maxRob(i): 
            if i in memo:
                return memo[i]
            elif i == 0:
                memo[i] = nums[i]
            elif i == 1:
                memo[i] = max(nums[0], nums[1])
            else:
                memo[i] = max(nums[i] + maxRob(i - 2), maxRob(i - 1))
            return memo[i]

        return maxRob(len(nums) - 1)
        
        
    
        


            

        


        