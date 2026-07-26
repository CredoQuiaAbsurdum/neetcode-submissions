class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        def countOnesAndZeros(string):
            one, zero = 0, 0
            for c in string:
                if c == '1':
                    one += 1
                else:
                    zero += 1
            return one, zero
        
        result = 0
        memo = {}
        def helper(i, zeros, ones):
            if (i, zeros, ones) in memo:
                return memo[(i, zeros, ones)]
            if i == len(strs):
                return 0

            current_ones, current_zeros = countOnesAndZeros(strs[i])
            
            # Option 1: Skip current string
            result = helper(i + 1, zeros, ones)
            
            # Option 2: Include current string (if budget allows)
            if zeros + current_zeros <= m and ones + current_ones <= n:
                result = max(result, 1 + helper(i + 1, zeros + current_zeros, ones + current_ones))
            
            memo[(i, zeros, ones)] = result
            return result
        
        return helper(0, 0, 0)