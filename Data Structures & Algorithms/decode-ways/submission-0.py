class Solution:
    def numDecodings(self, s: str) -> int:

        # 1 - 26
        # leading zero

        memo = {-1: 1}

        def helper(i):
            if i in memo: 
                return memo[i]
            if i < 0:
                return 1
            
            count = 0
            if s[i] != '0':
                count += helper(i - 1)
            
            if i > 0 and s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                count += helper(i - 2)
            
            memo[i] = count
            return count

        return helper(len(s) - 1)