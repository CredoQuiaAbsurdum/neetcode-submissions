class Solution:
    def hammingWeight(self, n: int) -> int:
        
        curr, i = n, 31
        count = 0
        while curr > 0:
            temp = 2 ** i
            if temp <= curr:
                curr -= temp
                count += 1
            i -= 1

        return count