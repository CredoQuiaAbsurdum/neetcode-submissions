class Solution:
    def hammingWeight(self, n: int) -> int:
        
        curr = n
        count = 0
        while curr > 0:
            curr &= curr - 1
            count += 1

        return count